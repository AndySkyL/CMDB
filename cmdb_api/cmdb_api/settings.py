"""
Django settings for cmdb_api project.

Generated by 'django-admin startproject' using Django 1.11.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!@a9x+5n159cvuwa4c1hgom%&pq9#1f_k^7hva#b6&vq_hzsm9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'stark.apps.StarkConfig',
    'rest_framework',
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

ROOT_URLCONF = 'cmdb_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'cmdb_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

DATETIME_FORMAT = 'Y-m-d H:i:s'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]


# API验证的key

API_KEY = '123456'

RSA_PRI_KEY = b'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlDWVFJQkFBS0JnUUNLTUxYUHVtNFF6SjlhMFE3Qld5U2J6QWlhS25zVlFzUDdyTTdOdzZRNXBFSlpqOGNBCjJTdXhXR0JMYk5PU0piSlBRQTcxUUlxWVd3R0c0YmZ6cnRvTzRJMGpBU25qNHlhUHBOSU8rZjFLeXNnZnUwRHkKZWRTL2RkeVNpSHQ1azNMRXIvcTBaZlR6Vkk0aG1UMDVyV2Rhd2xtYys2YzJ0TWQwMWpkNnNSSTJNUUlEQVFBQgpBb0dCQUlZZVhIYXQ0K0VlRjVOV3oxRk9HaXV6VEs0RGlNM0xyTlo0azRZVTJUQ3dnVXpYUkRkSWp5VmlOcU05CmplR01BSkQyQlE1Mmc0ejIxbmFJWHkzSGgyWUJBSTkzQThoRFh5WVNvdXB1TVplMVQ1OGlKMm0xN2FrckVHa1kKWjJKaVJFU0JIN2tqZThuRnljM2RFcCt2R3k0QVRwQVR1UFE4N2RCbXp4UVlVUVo1QWtVQWpOcnJHZFM3ZDlRaApYOGtBOWRZdHJZeVNnMVhUeC9kbVBWazRkdk5IbHAyY0V1OXJROWZoemJna3R0SkE1MGxIRFJjTzVuRElIeHBKCk15RnI1cDA5cHFQTXJ3c0NQUUQ3S0J0djZxSTJiM283WGgzaWwzNkprNXlYbmo0ejQ4SHFJc2pPRzF1WUNPSjgKYVVwVnRxSmEydDZKMjZzL0E3SHJSSWszQ1pSWk5rQTBaVE1DUkROcnRBb2hERE1wb09scjRzcmNYcDZOdytybwpTVUVtQXhBQVkwbWhkSS82aDhDdDRMWEt1T2MyQTBrdXBuMEkxa1JrRjQ5dXV0QUg4NU1UNzJVb0lCcVdqNkdUCkFqMEEzZU8xT2M4bHVNb01SMThETUNsL2xiUmY2R1BadUtaRHI4TkRmVFFXVzkrZG1TUzhrN1ZqQXJuVFdpQkUKenN0STZQNEg3Q1ArZUVMQnZvaVpBa1FsQklCMHJ3Y3UrMFJ5L3V0SHg4WDZsR1RNZ3NXalVvcEx5S21xTmgzVgpiekM0UlZLc0hNeXpIT1kzeUxla1ZDMXhUOWxpOFd3cVZzOXBqMWJja3dOa25QNDNTZz09Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg=='