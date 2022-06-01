### Настройки для development, дополняет base.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['dev.4t-habr.ru', '127.0.0.1', '127.0.0.1:8000']
CSRF_TRUSTED_ORIGINS = ['https://dev.4t-habr.ru']

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