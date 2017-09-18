from django import template
from home.models import Footer

register = template.Library()


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


# Retrieves the top menu items
@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    items = parent.get_children().live().in_menu()
    for item in items:
        item.show_dropdown = has_menu_children(item)
        item.active = (calling_page.url.startswith(item.url) if calling_page else False)

    return {
        'calling_page': calling_page,
        'menuitems': items,
        'is_home': (calling_page.url == u'/' if calling_page else False),
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Get the visible children of a top-level menu item
@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    children = parent.get_children().live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the footer sitemap items
@register.inclusion_tag('tags/footer.html', takes_context=True)
def footer(context, parent):
    if Footer.objects.first():
        return {
            'menuitems': parent.get_children().live().in_menu(),
            'facebook_url': Footer.objects.first().facebook_url,
            'twitter_url': Footer.objects.first().twitter_url,
            # required by the pageurl tag that we want to use within this template
            'request': context['request'],
        }
    else:
        return {
            # required by the pageurl tag that we want to use within this template
            'request': context['request'],
        }
