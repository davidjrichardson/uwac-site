from wagtail.wagtailcore import hooks

from home import image_operations


@hooks.register('register_image_operations')
def register_desaturate_filter():
    return [
        ('desaturate', image_operations.DesaturationOperation)
    ]
