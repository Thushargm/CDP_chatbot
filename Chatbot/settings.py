import os
from pathlib import Path
from dotenv import load_dotenv
import openai  # Add this import for OpenAI API integration

# Load environment variables from .env file
load_dotenv(dotenv_path=r'C:\Users\mahes\OneDrive\Desktop\cdp_chatbot\.env', override=True)


# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent

# Debug settings
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1')

# Secret key for Django project
SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is required and not set.")

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required and not set.")

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if OPENAI_API_KEY:
    print(f"OpenAI API Key is loaded successfully: {OPENAI_API_KEY[:5]}...{OPENAI_API_KEY[-5:]}")
else:
    print("OpenAI API Key is NOT loaded. Please check your .env file!")

# Allowed hosts configuration
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatbot',  # Your chatbot app
    'sslserver',  # SSL support for local development
    'django_extensions',  # Useful debugging tools
]

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# URL configuration
ROOT_URLCONF = 'cdp_chatbot.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Correct path to templates folder
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

# WSGI application
WSGI_APPLICATION = 'cdp_chatbot.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False  # Disabled for local development
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'

# Internal IPs for Debug Toolbar
if DEBUG:
    INTERNAL_IPS = ['127.0.0.1', 'localhost', '172.17.0.1']

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'INFO',
    },
}

# OpenAI API Key print for debugging
print(f"OpenAI API Key: {OPENAI_API_KEY}")
