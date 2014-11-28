from prod import *

SECRET_KEY = 'LOLOL'
ALLOWED_HOSTS = ['*']
STATIC_ROOT = '/var/www/backend/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
