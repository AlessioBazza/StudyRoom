from base import *

SECRET_KEY = 'deeeev'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
