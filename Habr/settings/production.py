### Настройки для productive, дополняет base.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*.4t-habr.ru', '127.0.0.1', '127.0.0.1:8000']
CSRF_TRUSTED_ORIGINS = ['https://4t-habr.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = "4t-habr.ru"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_EMAIL_VERIFICATION = 'none'
DOMAIN_NAME = '4t-habr.ru'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_SUBJECT_PREFIX = "[4t-habr] "
# EMAIL_HOST_USER = 'i@4t-habr.ru'
# EMAIL_HOST_PASSWORD = 'admin'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
SERVER_EMAIL = os.getenv('SERVER_EMAIL')

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'user@domain')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'password')
