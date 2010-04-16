from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not 'django.contrib.auth.backends.RemoteUserBackend' in settings.AUTHENTICATION_BACKENDS:
    raise ImproperlyConfigured('django-login-as requires the RemoteUserBackend')