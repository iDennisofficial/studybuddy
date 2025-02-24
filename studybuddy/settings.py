from pathlib import Path
import os
from dotenv import load_dotenv
import psycopg2
import dj_database_url

# Define variables at the top
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
POSTGRES_LOCALLY = False




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^_(hiz*kkhcy8)b1ssh214)zghvs6e8f#=#q#boeaeb(c05@0="

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == "development":
    DEBUG = True
else:
    DEBUG = False


ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'studybuddy-web.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://studybuddy-web.up.railway.app']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base.apps.BaseConfig",
    "rest_framework",

]

AUTH_USER_MODEL = "base.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "studybuddy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = "studybuddy.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
load_dotenv()  # Load environment variables from .env file




# Default database configuration (local PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'studybuddydb',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('DB_PASSWORD', '12345'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Override for production or if POSTGRES_LOCALLY is True
if ENVIRONMENT == "production" or POSTGRES_LOCALLY==True:
    DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
MEDIA_URL = "userprofilepicture/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / "static/images/userprofilepicture"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
