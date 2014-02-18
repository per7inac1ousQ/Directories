import django.conf.global_settings as DEFAULT_SETTINGS
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
import os

"""
Django settings for telDirMgmt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Baseline LDAP configuration without groups. (ask yours from the LDAP supervisorrrr!!!!!!!!)
AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"

AUTH_LDAP_BIND_DN = "cn=django-agent,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "phlebotinum"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=example,dc=com",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
# or perhaps:
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

AUTH_LDAP_PROFILE_ATTR_MAP = {
    "employee_number": "employeeNumber"
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True


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
	'crispy_forms',
	'crispy_forms_foundation', #use this to implement specific template layout for use with the Foundation responsive web-design framework
	'django_tables2',
	'south',
	'bootstrap3', #twitter bootstrap app for mobile development
	'django_filters', # use it to create filters e.x. search function (Maybe use it to find and delete items as well)
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

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'praktiki-uomdb',
		'USER': 'praktikos',
		'PASSWORD': 'patuom123!',
		'HOST': '195.251.213.90',
		'PORT': '3306',
		'OPTIONS': {
					#'charset': 'windows-1253'
					'charset' : 'utf8',
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
