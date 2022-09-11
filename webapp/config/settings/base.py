"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from datetime import timedelta

import environ
from config.utils import create_directory_if_not_exists, create_file_if_not_exists

BASE_DIR = environ.Path(__file__) - 3

env = environ.Env()
env.read_env(f"{BASE_DIR}/.env")

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG") == "True"

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    "jazzmin",  # ADMIN CUSTOM PACKAGE
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PACKAGE_APPS = [
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "corsheaders",
    "django_filters",
    "django_extensions",
]

PROJECT_APPS = [
    "user",
    "point",
    "notification",
    "challenge",
    "article",
    "file_manager",
    "item",
    "feedback",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + PACKAGE_APPS

DJANGO_MIDDLEWARES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

PACKAGE_MIDDELWARES = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

MIDDLEWARE = DJANGO_MIDDLEWARES + PACKAGE_MIDDELWARES

REST_USE_JWT = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=31),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

SITE_ID = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "none"
ROOT_URLCONF = "config.urls"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": env("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "user", "staticfiles"),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "config.authentications.CsrfExemptSessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "config.paginations.DefaultPagination",
    "EXCEPTION_HANDLER": "config.exceptions.api_exception_handler",
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ),
}

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "user.serializers.UserSerializer",
    "JWT_SERIALIZER": "user.serializers.UserJWTSerializer",
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

JAZZMIN_SETTINGS = {
    "site_title": "PeacePiece",
    "site_header": "PeacePiece",
    "site_brand": "PeacePiece",
}

LOG_DIR_PATH = os.path.join(BASE_DIR, "logs/")
SQL_LOG_FILE_PATH = os.path.join(BASE_DIR, "logs/sql_logfile.log")
WEB_LOG_FILE_PATH = os.path.join(BASE_DIR, "logs/logfile.log")

create_directory_if_not_exists(str(LOG_DIR_PATH))
create_file_if_not_exists(str(SQL_LOG_FILE_PATH))
create_file_if_not_exists(str(WEB_LOG_FILE_PATH))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "logFormat": {
            "format": "{levelname} ... [{name}:{lineno}] {asctime} {message}",
            "datefmt": "%d/%b/%Y %H:%M:%S",
            "style": "{",
        },
    },
    "handlers": {
        "sql_logger": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "logFormat"},
        "web_logger": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "logFormat",
        },
        "sql_log_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": SQL_LOG_FILE_PATH,
            "formatter": "logFormat",
        },
        "web_log_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": WEB_LOG_FILE_PATH,
            "formatter": "logFormat",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": [
                "sql_logger",
                "web_logger",
                "sql_log_file",
                "web_log_file",
            ],
            "level": "DEBUG",
            "formatter": "logFormat",
        },
    },
}

CSRF_TRUSTED_ORIGINS = ["https://*.peacepiece.in"]
