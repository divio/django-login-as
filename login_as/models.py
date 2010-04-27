from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not 'login_as.auth_backend.LoginAsBackend' in settings.AUTHENTICATION_BACKENDS:
    raise ImproperlyConfigured('django-login-as requires the login_as.auth_backend.LoginAsBackend')