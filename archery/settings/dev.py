from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

COMPRESS_ENABLED = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+&3a^7nypjh%t(_fjhr95l5#-k)!9_o7@1b#0pphp$=a(@_3+'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
