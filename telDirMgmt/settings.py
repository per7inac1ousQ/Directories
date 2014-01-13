import django.conf.global_settings as DEFAULT_SETTINGS
"""
Django settings for telDirMgmt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'foundation'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't_2tob1#mgc_dm_-fv6exu_ze!%9pu^n@=)dkg$*lwoxd*w26+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['195.251.213.61']

INTERNAL_IPS = ('195.251.213.61', )

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Directories',
	'Directories.templatetags.dir_extras',
<<<<<<< HEAD
	'crispy_forms',
	'crispy_forms_foundation', #use this to implement specific template layout for use with the Foundation responsive web-design framework
	'django_tables2',
=======
>>>>>>> afa76c68ac52b11cb70ac2e2a930c939c00d4e7f
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'telDirMgmt.urls'

WSGI_APPLICATION = 'telDirMgmt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'praktiki-uomdb',
		'USER': 'praktikos',
		'PASSWORD': '***',
		'HOST': '195.251.213.90',
		'PORT': '3306',
		'OPTIONS': {
                    'charset': 'latin1',
					#'charset': 'windows-1253'
					#'charset' : 'utf8',
                    'use_unicode': True, },#greek_general_ci
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/var/www/django-petros/static/',
)
