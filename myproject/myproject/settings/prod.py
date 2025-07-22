"""
Production Django settings for myproject.
"""

# flake8: noqa

import os

from .base import *
from .log.config import configure_logging

assert 'secret' not in SECRET_KEY, (
    'Please set a proper SECRET_KEY in production.')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    f"https://{HOSTNAME}",
]

# Use manifest to manage static file versions for cache busting:
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": ('django.contrib.staticfiles.storage'
                    '.ManifestStaticFilesStorage'),
    },
}

# Logging configuration
LOGGING = configure_logging(LOG_ROOT)
