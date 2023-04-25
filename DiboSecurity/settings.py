from pathlib import Path
from django.urls import reverse_lazy
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-@esgxw^z=*f#@34_%)%-hb4n^46d*0!!tw9!4#97!q@9gud(md'
SITE_ID = 1
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'webpack_loader',
    'DiboSecurity',
    'dapp',
    'dauth',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.gzip.GZipMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'DiboSecurity.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'DiboSecurity.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dibo_security',
        'USER': 'dibo_admin',
        'PASSWORD': 'Kode1234!',
        'HOST': '127.0.0.1',
        'PORT': 5433,
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

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

LANGUAGE_CODE = 'da-DK'
TIME_ZONE = 'Europe/Copenhagen'
USE_I18N = True
USE_TZ = True

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = reverse_lazy("frontpage")
LOGOUT_REDIRECT_URL = reverse_lazy("frontpage")

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "assets",
]
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static_root"
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media_root"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MESSAGE_TAGS = {
    messages.INFO: 'info',
    40: 'danger',
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'STATS_FILE': BASE_DIR / 'webpack-stats.json',
        'POLL_INTERVAL': 0.1,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap5'
