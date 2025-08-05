"""
Django settings for coreflowepc project.
Optimized for Heroku deployment with proper error handling.
"""

from pathlib import Path
import os
import dj_database_url

# Import env.py only if it exists (for local development)
try:
    if os.path.isfile('env.py'):
        import env
except ImportError:
    pass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-development-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Detect if running on Heroku
ON_HEROKU = 'DYNO' in os.environ

# Generate secure SECRET_KEY if not provided on Heroku
if ON_HEROKU and not os.environ.get('SECRET_KEY'):
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*(-_=+)'
    SECRET_KEY = ''.join(secrets.choice(alphabet) for i in range(50))
    print(f"🔑 Generated SECRET_KEY for Heroku deployment")

# Debug info for Heroku
if ON_HEROKU:
    print(f"🚀 Running on Heroku, DEBUG={DEBUG}")
    print(f"🔧 SECRET_KEY configured: {'Yes' if os.environ.get('SECRET_KEY') else 'Generated'}")
    print(f"🗄️  DATABASE_URL configured: {'Yes' if os.environ.get('DATABASE_URL') else 'No'}")

ALLOWED_HOSTS = ['*'] if DEBUG else ['.herokuapp.com', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'casestudy',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'coreflowepc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'coreflowepc.wsgi.application'

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3")

try:
    database_config = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    DATABASES = {'default': database_config}
    
    # Fix for Heroku Postgres SSL requirement
    if 'DATABASE_URL' in os.environ:
        DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
        
except Exception as e:
    # Fallback to SQLite if database URL parsing fails
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if ON_HEROKU:
    # Heroku production settings
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # Add additional staticfiles directories for Heroku
    STATICFILES_DIRS = []
else:
    # Development settings
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise configuration for serving media files on Heroku
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
# Important: Allow WhiteNoise to serve all file types including images
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'ico', 'woff', 'woff2']
# Additional MIME types for images
WHITENOISE_MIMETYPES = {
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg', 
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.webp': 'image/webp',
    '.ico': 'image/x-icon',
}
# Add media files to WhiteNoise on Heroku
if ON_HEROKU:
    # Configure WhiteNoise to serve uploaded files from static directory
    WHITENOISE_ROOT = os.path.join(STATIC_ROOT, 'uploads')
    WHITENOISE_INDEX_FILE = True
    # Ensure static files include uploaded content
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'static', 'uploads'))
    # Force HTTPS for static files on Heroku
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = False  # Let Heroku handle SSL redirect

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Simplified logging for Heroku - Force errors to show
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Show everything
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Show everything
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Show all request errors
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Force DEBUG mode for better error reporting temporarily
if ON_HEROKU:
    DEBUG = False  # Restore proper production setting
    ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1', 'localhost']

# Email configuration
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Use console backend in production if no email settings provided
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Additional allauth settings for production
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_USERNAME_MIN_LENGTH = 4

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
