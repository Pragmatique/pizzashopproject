"""
Django settings for pizzashopproject project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xp))p%52yz!*=z)=$!*4i-wyl^2f1z^hh61@i#ttddo7ev^j@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['damp-chamber-45738.herokuapp.com','localhost','127.0.0.1:8000',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    #'oauth2_provider',
    #'social_django',
    #'rest_framework_social_oauth2',

    'bootstrap3',

    'pizzashopapp',
    'django_angular_token_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pizzashopproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [ #'django_angular_token_auth/templates',
                    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
                  #  os.path.join(BASE_DIR, 'django_angular_token_auth/templates'),

                 # os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
                 # os.path.join(os.path.dirname(__file__), 'django_angular_token_auth/templates').replace('\\','/'),
                 # os.path.join(os.path.dirname(__file__), 'pizzashopapp','templates').replace('\\','/'),
                 # os.path.join(os.path.dirname(__file__), 'django_angular_token_auth','templates').replace('\\','/'),
                 # os.path.join(BASE_DIR, 'django_angular_token_auth/templates'),


                 ],
        #'APP_DIRS': True,

        'OPTIONS': {
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                #'admin_tools.template_loaders.Loader'
            ],
        },
    },
]

TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
#django.template.loaders.eggs.Loader',
)



TEMPLATE_DIRS = (

    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'django_angular_token_auth/templates').replace('\\','/'),
    os.path.join(BASE_DIR, 'django_angular_token_auth/templates'),
    os.path.join(os.path.dirname(__file__), 'pizzashopapp','templates').replace('\\','/'),
    os.path.join(os.path.dirname(__file__), 'django_angular_token_auth','templates').replace('\\','/'),
)


WSGI_APPLICATION = 'pizzashopproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')


import dj_database_url
db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)

# AUTHENTICATION_BACKENDS = (
#    'rest_framework_social_oauth2.backends.DjangoOAuth2',
#    'django.contrib.auth.backends.ModelBackend',
# )

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
   )
}

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1/24/6)
}