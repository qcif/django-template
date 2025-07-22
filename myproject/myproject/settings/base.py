"""
Base Django settings for myproject.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from utils.paths import ensure_dir

load_dotenv('../.env', override=True)

HOSTNAME = os.environ.get('HOSTNAME')

if not HOSTNAME:
    raise EnvironmentError("HOSTNAME must be declared in .env file")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-t(=mk32=eq-%taitgntl81a5c9o_g+yb%r3hpqx)ccv4j2dk42'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    HOSTNAME,
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Custom User Model
AUTH_USER_MODEL = 'accounts.User'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'app/media'
LOG_ROOT = ensure_dir(BASE_DIR / 'app/logs')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('MAIL_HOSTNAME')
EMAIL_PORT = os.environ.get('MAIL_SMTP_PORT')
EMAIL_HOST_USER = os.getenv('MAIL_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('MAIL_SMTP_PASSWORD')
EMAIL_USE_TLS = os.getenv('MAIL_USE_TLS', '').lower() in ('1', 'true')
EMAIL_FROM_ADDRESS = os.environ.get('MAIL_FROM_ADDRESS')
EMAIL_TO_ADDRESS = os.environ.get('MAIL_TO_ADDRESS')
SERVER_EMAIL = os.environ.get('MAIL_FROM_ADDRESS')
EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX',
                                 'Galaxy Labs Engine: ')

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_SITE_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_SECRET_KEY', '')

LOGOUT_REDIRECT_URL = '/'
