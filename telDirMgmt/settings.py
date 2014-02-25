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
'''
# TEST LDAP configuration start
<<<<<<< HEAD
# Baseline LDAP configuration without groups.
AUTH_LDAP_SERVER_URI = "ldap://ldap.testathon.net:389/"
AUTH_LDAP_BIND_DN = "" #"cn=stuart,ou=Users,dc=testathon,dc=net" Anonymous bind
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=testathon,dc=net",
ldap.SCOPE_SUBTREE, "(uid=%(user)s)") # test LDAP ---> "ou=users,dc=testathon,dc=net"
# uncomment below for direct bind
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

#Groups config
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=users,dc=testathon,dc=net",
ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=users,dc=testathon,dc=net" #allow authentication of this group
#AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=users,dc=testathon,dc=net" #deny authentication of this group

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
"first_name": "givenName",
"last_name": "sn",
"email": "mail"
}

AUTH_LDAP_START_TLS = True

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
'django.core.context_processors.request',
)

AUTH_LDAP_CONNECTION_OPTIONS = {
ldap.OPT_DEBUG_LEVEL: 0,
ldap.OPT_REFERRALS: 0,
}
# TEST LDAP configuration end
'''

# UOM LDAP configuration
# Baseline LDAP configuration without groups.
AUTH_LDAP_SERVER_URI = "ldaps://selene.uom.gr:636" # test LDAP ---> "ldap://ldap.testathon.net:389/"
AUTH_LDAP_BIND_DN = "uid=dummy,ou=People,o=uom,c=gr" #"cn=stuart,ou=Users,dc=testathon,dc=net"
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("o=uom,c=gr",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)") # test LDAP ---> "ou=users,dc=testathon,dc=net"
# uncomment below for direct bind
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

#Groups config
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=People,o=uom,c=gr",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

#AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=People,o=uom,c=gr" #allow authentication of this group
=======
# Baseline LDAP configuration without groups. 
AUTH_LDAP_SERVER_URI = "ldap://ldap.testathon.net:389/"
AUTH_LDAP_BIND_DN = "" #"cn=stuart,ou=Users,dc=testathon,dc=net" Anonymous bind
AUTH_LDAP_BIND_PASSWORD = "" 
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=testathon,dc=net",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")  # test LDAP ---> "ou=users,dc=testathon,dc=net"
# uncomment below for direct bind
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

#Groups config
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=users,dc=testathon,dc=net",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=users,dc=testathon,dc=net" #allow authentication of this group
>>>>>>> 40ee6f394d51dce5deafcaf37239451632112061
#AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=users,dc=testathon,dc=net" #deny authentication of this group

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

<<<<<<< HEAD
=======
AUTH_LDAP_START_TLS = True

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

AUTH_LDAP_CONNECTION_OPTIONS = {
        ldap.OPT_DEBUG_LEVEL: 0,
        ldap.OPT_REFERRALS: 0,
}
# TEST LDAP configuration end
'''

# UOM LDAP configuration
# Baseline LDAP configuration without groups. 
AUTH_LDAP_SERVER_URI = "ldaps://selene.uom.gr:636"  # test LDAP ---> "ldap://ldap.testathon.net:389/"
AUTH_LDAP_BIND_DN = "uid=dummy,ou=People,o=uom,c=gr" #"cn=stuart,ou=Users,dc=testathon,dc=net" 
AUTH_LDAP_BIND_PASSWORD = "wwwtest" 
AUTH_LDAP_USER_SEARCH = LDAPSearch("o=uom,c=gr",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")  # test LDAP ---> "ou=users,dc=testathon,dc=net"
# uncomment below for direct bind
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

#Groups config
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=People,o=uom,c=gr",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

#AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=People,o=uom,c=gr" #allow authentication of this group
#AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=users,dc=testathon,dc=net" #deny authentication of this group

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

>>>>>>> 40ee6f394d51dce5deafcaf37239451632112061
AUTH_LDAP_START_TLS = False

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTH_LDAP_CONNECTION_OPTIONS = {
        ldap.OPT_DEBUG_LEVEL: 0,
        ldap.OPT_REFERRALS: 0,
}

# UOM LDAP configuration end

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
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
<<<<<<< HEAD
'Directories.templatetags.dir_extras',
'crispy_forms',
'crispy_forms_foundation', # has foundation responsive web design... don't you have bootstrap for this??
'django_tables2', # table creation..... maybe delete??
'south', # database migration
'haystack', # search engine
'bootstrap3', #twitter bootstrap app for mobile development
'django_filters', # use it to create filters e.x. search function (Maybe use it to find and delete items as well)
#'debug_toolbar',
=======
	'Directories.templatetags.dir_extras',
	'crispy_forms',
	'crispy_forms_foundation', # has foundation responsive web design... don't you have bootstrap for this??
	'django_tables2', # table creation..... maybe delete??
	'south', # database migration
	'haystack', # search engine
	'bootstrap3', #twitter bootstrap app for mobile development
	'django_filters', # use it to create filters e.x. search function (Maybe use it to find and delete items as well)
	#'debug_toolbar',
>>>>>>> 40ee6f394d51dce5deafcaf37239451632112061
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
'PASSWORD': '',
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

# security when using cookies. Not sure how to use them
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        #'PATH': '/usr/local/lib/python2.7/dist-packages/whoosh/',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        #'PATH': '/usr/local/lib/python2.7/dist-packages/whoosh/index.py', #'/home/search/whoosh_index',
       'STORAGE': 'file',
        'POST_LIMIT': 128 * 1024 * 1024,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
        'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    },
}
<<<<<<< HEAD
=======

>>>>>>> 40ee6f394d51dce5deafcaf37239451632112061
