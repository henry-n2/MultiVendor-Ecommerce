# """
# Django settings for ecommerce project.

# Generated by 'django-admin startproject' using Django 4.2.5.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/4.2/ref/settings/
# """
# import dj_database_url
# from pathlib import Path
# import os
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# # SECRET_KEY = 'django-insecure-!bp990y8wp4pt^hm^5%$68jvn@9+@9^_z8(7e+2=lyob9fz!z%'

# SECRET_KEY = os.environ.get("SECRET_KEY")
# # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = True
# DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# # CSRF_TRUSTED_ORIGINS = [
# #     "https://multivendor-ecommerce-j8lb.onrender.com",
# #     "http://localhost:8000",
# # ]



# ALLOWED_HOSTS = ['*']
# # ALLOWED_HOSTS = []

# # Application definition

# INSTALLED_APPS = [
#     'colorfield',
#     'jazzmin',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'home',
#     'accounts',
#     'products.apps.ProductsConfig',
#     'AdminPanel',
#     'Vendors',
#     'django_ckeditor_5',
#     'payments',
#     'prediction',
#     'about'
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'ecommerce.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR /'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'ecommerce.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#         # 'ENGINE': 'django.db.backends.postgresql',
#         # 'NAME': 'ecogridai',
#         # 'USER': 'ecogridai_user',
#         # 'PASSWORD': 'w69V3yaVbyYpaPQ3R45ctQLoJQ5tRSIE',
#         # 'HOST': 'dpg-cvo6aimmcj7s73fucs60-a',  # <- This is the problem
#         # 'PORT': '5432',
#     }
# }

# # url="postgresql://ecogridai_user:w69V3yaVbyYpaPQ3R45ctQLoJQ5tRSIE@dpg-cvo6aimmcj7s73fucs60-a/ecogridai"
# DATABASES["default"] = dj_database_url.parse("postgresql://ecogridai_user:w69V3yaVbyYpaPQ3R45ctQLoJQ5tRSIE@dpg-cvo6aimmcj7s73fucs60-a.oregon-postgres.render.com/ecogridai")

# # Password validation
# # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.2/howto/static-files/

# # STATIC_URL = 'static/'
# # # STATICFILES_DIRS = [BASE_DIR / "static"]
# # # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # MEDIA_URL = 'images/'
# # MEDIA_ROOT = BASE_DIR / 'media'
# # STATIC_URL = '/static/'
# # This production code might break development mode, so we check whether we're in DEBUG mode
# # if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
# #     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
#     # and renames the files with unique names for each version to support long-term caching
#     # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Default primary key field type
# # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'accounts.CustomUser'

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend', 
# ]

# APPEND_SLASH=False


import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-!bp990y8wp4pt^hm^5%$68jvn@9+@9^_z8(7e+2=lyob9fz!z%'
# Hardcoded secret key (Not recommended for production)
# SECRET_KEY = os.environ.get("SECRET_KEY")

# Toggle this manually for prod/dev
DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    "https://multivendor-ecommerce-j8lb.onrender.com",
    "http://localhost:8000",
]


ALLOWED_HOSTS = ['*']  # Use specific domain(s) in production

# Apps
INSTALLED_APPS = [
    'colorfield',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'accounts',
    'products.apps.ProductsConfig',
    'AdminPanel',
    'Vendors',
    # 'django_ckeditor_5',
    'ckeditor',
    'payments',
    'prediction',
    'about',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if not DEBUG:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

ROOT_URLCONF = 'ecommerce.urls'

# Templates
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database - Use SQLite locally or PostgreSQL for Render
# Comment/uncomment depending on where you're running it

# --- LOCAL ---
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# --- DEPLOYMENT (Render PostgreSQL) ---
DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://ecogridai_user:w69V3yaVbyYpaPQ3R45ctQLoJQ5tRSIE@dpg-cvo6aimmcj7s73fucs60-a.oregon-postgres.render.com/ecogridai"
    )
}

# Password validation
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

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and Media
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Other Settings
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

APPEND_SLASH = False


