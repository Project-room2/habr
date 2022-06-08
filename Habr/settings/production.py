### Настройки для productive, дополняет base.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['4t-habr.ru', '127.0.0.1', '127.0.0.1:8000']
CSRF_TRUSTED_ORIGINS = ['https://4t-habr.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DOMAIN_NAME = '4t-habr.ru'
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
SERVER_EMAIL = os.getenv('SERVER_EMAIL')

EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_SUBJECT_PREFIX = "[4t-habr] "
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = '4t-habr <i@4t-habr.ru>'
