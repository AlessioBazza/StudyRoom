from base import *

# set this in __init__.py
# SECRET_KEY = ...

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = '/var/www/django-static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
