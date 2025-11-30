from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1" ]
# You can add more local settings here

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
