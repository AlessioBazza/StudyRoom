from base import *

# set thes in __init__.py
# SECRET_KEY = ...
# DATABASES = { ... }

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = '/var/www/django-static'
ALLOWED_HOSTS = ['studyroom.noip.me']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
