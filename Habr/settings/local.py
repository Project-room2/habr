### Настройки для локальной разработки, дополняет base.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.1:8000']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1']

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('db.sqlite3'),
    }
}


ACCOUNT_EMAIL_VERIFICATION = 'none'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'