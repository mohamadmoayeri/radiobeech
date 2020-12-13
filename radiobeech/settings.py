"""
Django settings for podcast project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bb--jho(5+jm)(coy7j+65%4)&x0%8p6p$l66(^zccfuajxo7z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'edit',
    'home',
    'profiles',
    'accounts',
    'ckeditor',
    'django_cleanup',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #Manages sessions across requests
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', #Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edit.middlewares.loginrequired',
]
#CACHE_MIDDLEWARE_ALIAS = 'default'  # which cache alias to use
#CACHE_MIDDLEWARE_SECONDS = 300    # number of seconds to cache a page for (TTL)
#CACHE_MIDDLEWARE_KEY_PREFIX = ''    # should be used if the cache is shared across multiple sites that use the same Django instance

ROOT_URLCONF = 'radiobeech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'radiobeech.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'beech',
        'PASSWORD':'191431',
        'USER':'mhmd',
        'HOST':'postgre',
        #'port':'5432',
        
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}





CACHES = {
     'default':
      { 'BACKEND': "django.core.cache.backends.memcached.MemcachedCache", 'LOCATION': 'memcached'}
      #{'BACKEND':'django.core.cache.backends.db.DatabaseCache', 'LOCATION': 'my_cache_table', }

}






# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mohammad.moayyeri10@gmail.com'
EMAIL_HOST_PASSWORD = 'xxkvvrdsdulsvhmf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')

MEDIA_URL = '/image/' or '/story/' or '/avatar/'
MEDIA_ROOT=os.path.join(BASE_DIR,'')





#ckeditor setting
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "uploads/"



LOGIN_REDIRECT_URL = 'home/'
LOGOUT_REDIRECT_URL = 'home/'


RENDERER = ('rest_framework.renderers.JSONRenderer', )
#if DEBUG:
#    RENDERER += ('rest_framework.renderers.BrowsableAPIRenderer', )


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),

    #'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',
    #                            'rest_framework.filters.SearchFilter',
    #                            'rest_framework.filters.OrderingFilter'),

#    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#                                'PAGE_SIZE': 2,

    'DEFAULT_RENDERER_CLASSES': RENDERER


}






