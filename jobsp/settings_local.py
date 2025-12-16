
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable some complex middleware for local dev if they cause issues
# MIDDLEWARE = [m for m in MIDDLEWARE if 'subdomain' not in m]

ALLOWED_HOSTS = ['*']

# Override Redis requirement for Celery to run locally without it if needed (optional)
# For now, we assume user might handle redis or we just let it fail gracefully if not running.
CELERY_BROKER_URL = 'memory://'
CELERY_RESULT_BACKEND = 'db+sqlite:///' + os.path.join(BASE_DIR, 'celery-db.sqlite3')
