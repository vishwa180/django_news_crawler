from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(5m21m6^atzdweou&f4$dkmmvbuqr7&eri!rm&^xpvml)_93mj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
    'rest_framework.authtoken',
    'news',
    'celery'
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

ROOT_URLCONF = 'django_news_crawler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_news_crawler.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Logging Configuration

LOGS_DIR = os.path.join(os.path.join(BASE_DIR, '../logs/'))


def get_log_directory():
    if not os.path.exists(LOGS_DIR):
        os.mkdir(LOGS_DIR)
    return LOGS_DIR


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_format': {
            'format': ' {asctime} :: {levelname} ::  {pathname} :: {message}',
            'style': '{',
        },
        'request_format': {
            'format': ' {asctime} :: {message}',
            'style': '{',
        },
        'exception_format': {
            'format': ' {asctime} :: {levelname} ::  {pathname} :: {lineno} :: {message}',
            'style': '{',
        }
    },
    'handlers': {
        'default_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(get_log_directory(), 'application.log'),
            'formatter': 'default_format',
            'encoding': 'utf8',
            'when': 'D',
            'interval': 1,
            'backupCount': 30,
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(get_log_directory(), 'requests.log'),
            'formatter': 'request_format',
            'encoding': 'utf8',
            'when': 'D',
            'interval': 1,
            'backupCount': 30,
        },
        'template_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(get_log_directory(), 'templates.log'),
            'encoding': 'utf8',
            'when': 'D',
            'interval': 1,
            'backupCount': 30,
        },
        'backend_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(get_log_directory(), 'database.log'),
            'formatter': 'request_format',
            'encoding': 'utf8',
            'when': 'D',
            'interval': 1,
            'backupCount': 30,
        },
        'exception_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(get_log_directory(), 'exception.log'),
            'formatter': 'exception_format',
            'encoding': 'utf8',
            'when': 'D',
            'interval': 1,
            'backupCount': 30,
        }
    },
    'loggers': {
        'default_logger': {
            'handlers': ['default_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['template_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.db.backends': {
            'handlers': ['backend_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'exception_logger': {
            'handlers': ['exception_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
