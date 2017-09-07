from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
SECRET_KEY = 'your_secret_key_here'

try:
    from .local import *
except ImportError:
    pass


# SASS Compression
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
