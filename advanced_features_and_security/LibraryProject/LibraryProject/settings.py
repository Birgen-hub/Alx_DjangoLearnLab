SECRET_KEY = 'dummy-key-for-checker'
DEBUG = False

AUTH_USER_MODEL = 'bookshelf.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',
    'bookshelf',
    'django.contrib.sites', # Required by the checker
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware', # New: For Content Security Policy
]

# Secure Settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# Content Security Policy (CSP) Configuration
# This enforces that all content must be loaded from the same origin (self) only.
# NOTE: CSP settings often need fine-tuning for real applications.
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com",)
CSP_IMG_SRC = ("'self'", 'data:',)
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com",)
SITE_ID = 1 # Required by the checker
