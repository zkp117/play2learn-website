import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0^=_l^slk4l=b236-2q9+)5om$ge)%ovmz%@^fltsu)sgnww41'

DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS SECTION

INSTALLED_APPS = [
    # built-in django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',

    # local apps
    'pages.apps.PagesConfig',
    'anagramhunt.apps.AnagramhuntConfig',
    'mathfacts.apps.MathfactsConfig',
    'users.apps.UsersConfig',
    'contact.apps.ContactConfig',

    # third-party apps
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1

# CRISPY SECTION

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

# MIDDLEWARE SECTION

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'play2learn.urls'

# TEMPLATES SECTION

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'play2learn.wsgi.application'

# EMAIL SECTION 

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = 'neeneez2008@gmail.com'

ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'

# DATABASES SECTION 

DATABASES = {
    'default': { # 
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'p2l_scores',
        'USER': 'postgres',
        'PASSWORD': 'Pandora117!',
        'HOST': 'localhost',
        'PORT': 6623
    },
}

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

# AUTHENTICATION SETTINGS
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = '/'

## django-allauth settings
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # Default: 3
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Default: 'optional'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'  # Default: '/'
ACCOUNT_SIGNUP_REDIRECT_URL = 'pages:homepage'
ACCOUNT_AUTHENTICATED_REDIRECT_URL = 'pages:homepage'
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_RATE_LIMITS = {
    "login_failed": "5/m"  # Allows 5 failed login attempts per minute
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, even w/o `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth`-specific auth methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'users.CustomUser'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# BOTTOM OF settings.py
if os.environ.get('ENVIRONMENT') != 'production':
    from .local_settings import *
# DON'T PUT ANYTHING BELOW THIS
