import os
import sys

# Dynamically set project path
PROJECT_PATH, filename = os.path.split(__file__)
sys.path.append(PROJECT_PATH)

# Django settings for citysom project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nikhil Verma', 'varma.nikhil22@gmail.com'),
)

MANAGERS = ADMINS

# logging
import logging.config
#logging.config.fileConfig(os.path.join(PROJECT_PATH, "logger.cfg"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SITE_NAME = "Citysom"
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/charleshenri/memcached.sock',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_URL =  'http://www.citysom.com/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = "/home/charleshenri/webapps/citysom_static/"
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://www.citysom.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/charleshenri/webapps/django/citysom/citysom/media',
        
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ADMIN_MEDIA_PREFIX = '/admin/'

AUTH_PROFILE_MODULE = "myprofile.UserProfile"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_6dshm%f$m&amp;_-%=m_8i!g5gdwztdwi8!^*^piil^cgh0b_%2f!'

# Lis
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
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'citysom.processors.template_data',
)

ROOT_URLCONF = 'citysom.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'citysom.wsgi.application'

TEMPLATE_DIRS = (
     PROJECT_PATH + "/templates"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'citysom.registration',
    'citysom.event',
    'citysom.myprofile',
    'tinymce',
)

TINYMCE_JS_URL = MEDIA_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,paste",
    'mode' : "exact",
    'theme' : "advanced",
    'theme_advanced_buttons1':"bold,italic,underline,strikethrough,justifyleft,justifycenter,justifyright,justifyfull,undo,redo,bullist,numlist,outdent,indent,cut,copy,paste,image",
    'theme_advanced_buttons2': "tablecontrols",
    'theme_advanced_buttons3':"",
    'skin' : "o2k7",
    'skin_variant' : "silver",
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

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

import os.path
LOCAL_SETTINGS = os.path.join(os.path.dirname(__file__), "local_settings") + ".py"
if not os.path.exists(LOCAL_SETTINGS):
    msg = (
    """\nWarning: Can't find the expected local Django settings file:    \n%s\n"""
    % (LOCAL_SETTINGS)
    )
    print msg
    del msg
    SETTINGS_LOCAL = ""
else:
    # If this raises an exception, we simply let it bubble up.
    execfile(LOCAL_SETTINGS)
try:
    from local_settings import *
except:
    pass

HOST = "www.citysom.com"
