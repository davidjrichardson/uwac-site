from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

env = environ.Env()
environ.Env.read_env()

INSTALLED_APPS = INSTALLED_APPS + [
    'storages'
]

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_FILE_OVERWRITE = False

STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/'
STATICFILES_STORAGE = 'archery.settings.storage_backends.StaticStorage'
MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/'
DEFAULT_FILE_STORAGE = 'archery.settings.storage_backends.MediaStorage'
