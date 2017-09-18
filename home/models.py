from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailcore.models import Page


class HomePage(Page):
    # TODO: Subpage types

    description = models.TextField(max_length=400, default='')
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This is the image displayed on the home page as the first thing a user will see'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        ImageChooserPanel('cover_image')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)

        if self.cover_image:
            context['cover_image'] = self.cover_image.get_rendition('width-1536').url
        else:
            context['cover_image'] = None

        return context


@register_snippet
class Footer(models.Model):
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('facebook_url'),
        FieldPanel('twitter_url'),
    ]

    def __str__(self):
        return 'Footer URLs'
