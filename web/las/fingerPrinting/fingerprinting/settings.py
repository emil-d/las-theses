# Django settings for fingerprinting project.
from os import path
import os

BASEDIR = path.split(path.dirname(path.abspath(__file__)))[0]
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DB_NAME = 'fingerprinting'
DB_USERNAME = 'fingerusr'
DB_PASSWORD = 'fingerprintingpwd2013'
DB_HOST='lasmysql'
GRAPH_DB_HOST='lasneo4j'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
        'USER': DB_USERNAME,                      # Not used with sqlite3.
        'PASSWORD': DB_PASSWORD,                  # Not used with sqlite3.
        'HOST': DB_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

from utils import getLASUrl

DOMAIN_NAME=getLASUrl()


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = path.join(BASEDIR, 'profiling/profiling_media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/profiling_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

TEMP_URL = path.join(BASEDIR,'profiling/profiling_media/tmp/')

#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c!#h5#c1hq6am^k7j!2=il#avxl&amp;e1je255wp@d*m@@a+p2rds'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'profiling.middleware.AjaxRedirect',
    'api.middleware.XsSharingMiddleware',
    'api.middleware.ContentTypeMiddleware',
    'global_request_middleware.GlobalRequestMiddleware',
    'cookieMiddleware.ExtendUserSession',
)

ROOT_URLCONF = 'fingerprinting.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'fingerprinting.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'profiling',
    'LASAuth',
    'piston',
    'editpermission',
    'global_request_middleware',
    'cookieMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'LASAuth.auth.LASAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.core.context_processors.debug',
                                'django.core.context_processors.i18n',
                                'django.core.context_processors.media',
                                'profiling.context_processor.custom_context_processor',
)


TEMP_URL = path.join(BASEDIR,'profiling/profiling_media/tmp/')

LOGIN_URL = '/auth/startlogin/'
LAS_AUTH_SERVER_URL = DOMAIN_NAME + '/las/laslogin/'
LAS_URL = DOMAIN_NAME + '/las/'
LAS_AUTH_USE_HTTPS = True
THIS_APP_SHORTNAME='FPM'
AUTH_SECRET_KEY = 'n|iA!~ZlC!(#DIGRFbiAMSa7G+i!qSiKe`yn-ebHG?i-HKV6PRs{d{-Bc2!PUdzQ'
API_SHARED_KEY = 'u8Hk;GVTbW|siLN0([_gryt2/c)]G7@g$l}.@t?A+Sq/=2l||2ZVkV@w)9+uLQE('
SYNC_PERMISSIONS_URL= DOMAIN_NAME + '/las/syncPermissions/'
APPNAME = 'profiling'
USE_GRAPH_DB = True
GRAPH_DB_URL='http://'+GRAPH_DB_HOST+':7474/db/data/'


CSRF_COOKIE_PATH = '/fingerPrinting'
SESSION_COOKIE_PATH = '/fingerPrinting'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 14400

# to circumvent certificate verification on newer versions of urllib2/ssl
import ssl
#if hasattr(ssl, "_create_unverified_context"):
ssl._create_default_https_context=ssl._create_unverified_context

