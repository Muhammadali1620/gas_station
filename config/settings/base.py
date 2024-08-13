import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# (?<data>img/[a-zA-Z0-9/._-]+)
# {% static '${data}' %}

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS: True

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar',
    'corsheaders',
    'drf_yasg',
    'colorfield',
]

INSTALLED_APPS += [
    'apps.general.apps.GeneralConfig',
    'apps.users.apps.UsersConfig',
    'apps.authentication.apps.AuthenticationConfig',
    'apps.stations.apps.StationsConfig',
    'apps.cars.apps.CarsConfig',
    'apps.booking.apps.BookingConfig',
    'apps.orders.apps.OrdersConfig',
    'apps.wishlist.apps.WishlistConfig',
    'apps.appeals.apps.AppealsConfig',
    'apps.complaints.apps.ComplaintsConfig',
    'apps.notifications.apps.NotificationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'apps.general.middleware.LanguageMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


TIME_ZONE = 'Asia/Tashkent'

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'