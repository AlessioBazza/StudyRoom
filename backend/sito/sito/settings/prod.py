from base import *

#SECRET_KEY = '' # set this in __init__.py 
DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = '/var/www/backend/static'
STATIC_URL = '/'
ALLOWED_HOSTS = ['studyroom.philspark.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'set this in __init__.py',
        'USER': 'set this in __init__.py',
        'PASSWORD': 'set this in __init__.py',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
