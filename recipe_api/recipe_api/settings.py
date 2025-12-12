from pathlib import Path
SECRET_KEY = 'django-insecure-dummy-key-for-local-development-only'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'knox',

    'recipes',

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',

ROOT_URLCONF = 'recipe_api.urls'

TEMPLATES = [
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
        },
]

WSGI_APPLICATION = 'recipe_api.wsgi.application'
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
        'knox.auth.TokenAuthentication',
    ],
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
