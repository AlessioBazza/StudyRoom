import os
import pytz
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

ROOT_URLCONF = 'sito.urls'
WSGI_APPLICATION = 'sito.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

LANGUAGE_CODE = 'it'
TIME_ZONE = 'Europe/Rome'
TIMEZONE = pytz.timezone(TIME_ZONE)
POSTI_DISPLAY_INTERVAL = datetime.timedelta(hours=2)
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
