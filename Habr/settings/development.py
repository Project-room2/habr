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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DOMAIN_NAME = '4t-habr.ru'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
SERVER_EMAIL = os.getenv('SERVER_EMAIL')

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'user@domain')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password')
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = "[4t-habr] "
EMAIL_HOST_USER = 'root'
