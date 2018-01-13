from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django.utils import timezone
from modelcluster.fields import ParentalKey
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailcore.blocks import StructBlock, TextBlock, CharBlock, StreamBlock, RichTextBlock, PageChooserBlock
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class GalleryImage(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        help_text='This is the image displayed on the home page as the first thing a user will see'
    )
    attribution = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, blank=True)
    page = ParentalKey('GalleryPage', related_name='gallery_items')

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('attribution'),
        FieldPanel('caption')
    ]


class GalleryPage(Page):
    parent_page_types = ['home.GalleryIndexPage']

    date = models.DateTimeField('Gallery date', default=timezone.now)
    description = RichTextField(default='',
                                help_text='The description of the event or purpose of the gallery, displayed under the title')
    gallery_cover = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        help_text='This is the image displayed on the home page as the first thing a user will see'
    )

    @property
    def photos(self):
        return self.gallery_items.all()

    # This is required for the GalleryPage reference to work on the inline panel
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('description'),
            FieldPanel('date'),
            ImageChooserPanel('gallery_cover')
        ], heading='Gallery information'),
        InlinePanel('gallery_items', label='Gallery photos')
    ]


class PullQuoteBlock(StructBlock):
    quote = TextBlock('quote title')
    attribution = CharBlock()

    class Meta:
        icon = 'openquote'


class CreditImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(help_text='Photo caption', required=False)
    credit = TextBlock(help_text='Image credit')

    class Meta:
        icon = 'image'


class GalleryBlock(StructBlock):
    gallery = PageChooserBlock(target_model=GalleryPage)

    class Meta:
        icon = 'image'


class BlogStreamBlock(StreamBlock):
    h2 = CharBlock(icon='title', classname='title')
    h3 = CharBlock(icon='title', classname='title')
    h4 = CharBlock(icon='title', classname='title')
    paragraph = RichTextBlock(icon='pilcrow')
    image = CreditImageBlock()
    pullquote = PullQuoteBlock()
    gallery = GalleryBlock()
    document = DocumentChooserBlock(icon='doc-full-inverse')
    table = TableBlock(table_options={
        'startRows': 1,
        'startCols': 2
    })


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class GalleryIndexPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['home.GalleryPage']

    description = RichTextField(default='', blank=True)

    @property
    def galleries(self):
        return GalleryPage.objects.live().descendant_of(self).order_by('-date')

    content_panels = Page.content_panels + [
        FieldPanel('description')
    ]


class HomePage(Page):
    subpage_types = ['home.GalleryIndexPage', 'home.BlogPage', 'home.ContentPage']

    description = models.TextField(max_length=400, default='')
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This is the image displayed on the home page as the first thing a user will see'
    )
    cover_image_credit = models.CharField(blank=True,
                                          max_length=100,
                                          help_text='The author of the photograph for the image on the home page')

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        ImageChooserPanel('cover_image'),
        FieldPanel('cover_image_credit')
    ]

    @property
    def blogs(self):
        return BlogPage.objects.live().descendant_of(self).order_by('-date')

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)

        # Paginate the blog posts for infinite scroll
        paginator = Paginator(self.blogs, 5)
        try:
            blogs = paginator.page(request.GET.get('page', 1))
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context['blogs'] = blogs

        # Get the url for the cover image if there is one
        if self.cover_image:
            context['cover_image'] = self.cover_image.get_rendition('width-1536').url
        else:
            context['cover_image'] = None

        return context


class ContentPage(Page):
    parent_page_types = ['home.HomePage', 'home.ContentPage']
    subpage_types = ['home.ContentPage']

    body = StreamField(BlogStreamBlock)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    @property
    def is_child(self):
        return type(self.get_parent().specific) is not HomePage


class BlogPage(Page):
    parent_page_types = ['home.HomePage']

    body = StreamField(BlogStreamBlock)
    date = models.DateTimeField('Post date', default=timezone.now)
    excerpt = RichTextField(help_text='This is displayed on the home and blog listing pages', default='')
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This is the image displayed on the home page as the first thing a user will see'
    )
    cover_image_credit = models.CharField(blank=True, max_length=100, default='')

    content_panels = [
        MultiFieldPanel([
            FieldPanel('title', classname="full title"),
            FieldPanel('excerpt'),
            FieldPanel('date'),
            StreamFieldPanel('body')
        ], heading='Post content'),
        MultiFieldPanel([
            ImageChooserPanel('cover_image'),
            FieldPanel('cover_image_credit')
        ], heading='Blog post cover image')
    ]

    @property
    def further_reading(self):
        siblings = BlogPage.objects.live().sibling_of(self, inclusive=False).order_by('-date')
        latest = siblings.first()
        next_article = siblings.filter(date__lte=self.date).exclude(id=latest.id).order_by('-date').first()

        return [latest, next_article]


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
