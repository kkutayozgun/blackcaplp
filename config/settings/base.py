import os, environ
from django.utils.translation import ugettext_lazy as _

env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default='')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party Apps:
    'ckeditor',
    'rosetta',
    'parler',

    # Project Apps:
    'page',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db('DB_URL', default='sqlite:///db.sqlite3')
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

TIME_ZONE = env('TIME_ZONE', default='Europe/Istanbul')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')

MEDIA_URL = '/media/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

LANGUAGE_CODE = env('LANGUAGE_CODE', default="tr")

LANGUAGES = (
    ('tr', _('Türkçe')),
    ('en', _('English')),
    ('de', _('German')),
)

LANGUAGE_SESSION_KEY = 'language'

ADMIN_URL = env('ADMIN_URL', default="admin/")

PARLER_LANGUAGES = {
    None: (
        {'code': 'tr', },  # Turkish
        {'code': 'en', },  # English
        {'code': 'de', },  # German
    ),
    'default': {
        'fallbacks': ['tr'],
        'hide_untranslated': False,
    }
}

# ROSETTA_MESSAGES_PER_PAGE = 20
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = False
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'tr'
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = _('Türkçe')
ROSETTA_WSGI_AUTO_RELOAD = ROSETTA_UWSGI_AUTO_RELOAD = True
ROSETTA_SHOW_AT_ADMIN_PANEL = True

# EMAIL_HOST = env("EMAIL_HOST", default="")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
# EMAIL_PORT = env("EMAIL_PORT", default=587)
# EMAIL_USE_TLS=True

# DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)

# CONTACT_FORM_RECEIVER = env.list('CONTACT_FORM_RECEIVER', default="")
