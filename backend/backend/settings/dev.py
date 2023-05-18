from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SECURITY WARNING: change key before production! 
# manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY = "$ig7s*(jh*nqlfhcf-qxnc2x20s94ak9jojuet_0#md-*ncl_t"

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    ]

ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"




try:
    from .local import *
except ImportError:
    pass
