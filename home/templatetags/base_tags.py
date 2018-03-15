from django import template
from wagtail.core.models import Page

import mimetypes

from home.models import Footer

register = template.Library()


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


# Retrieves top-level menu items for the sidebar
@register.inclusion_tag('tags/side_menu.html', takes_context=True)
def side_menu(context, parent, calling_page=None):
    items = parent.get_children().live().in_menu()
    for item in items:
        item.show_drilldown = has_menu_children(item)
        item.active = (calling_page.url.startswith(item.url) if calling_page else False)

    return {
        'calling_page': calling_page,
        'menuitems': items,
        'is_home': (calling_page.url == u'/' if calling_page else False),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the top menu items
@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None, transparent=False):
    items = parent.get_children().live().in_menu()
    for item in items:
        item.show_dropdown = has_menu_children(item)
        item.active = (calling_page.url.startswith(item.url) if calling_page else False)

    return {
        'calling_page': calling_page,
        'menuitems': items,
        'is_home': (calling_page.url == u'/' if calling_page else False),
        'transparent': transparent,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Get the visible children of a top-level menu item
@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def nav_menu_children(context, parent, side_menu=False):
    children = parent.get_children().live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': children,
        'side_menu': side_menu,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the footer sitemap items
@register.inclusion_tag('tags/footer.html', takes_context=True)
def footer(context, parent, calling_page):
    if Footer.objects.first():
        return {
            'menuitems': parent.get_children().live().in_menu(),
            'facebook_url': Footer.objects.first().facebook_url,
            'twitter_url': Footer.objects.first().twitter_url,
            'calling_page': calling_page,
            # required by the pageurl tag that we want to use within this template
            'request': context['request'],
        }
    else:
        return {
            'calling_page': calling_page,
            # required by the pageurl tag that we want to use within this template
            'request': context['request'],
        }


@register.inclusion_tag('tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.filter
def get_image_mime_type(image):
    return mimetypes.guess_type(image.url)[0]


@register.filter
def is_portrait(image):
    return image.width < image.height


@register.filter
def more_than_one(collection):
    return len(collection) > 1
