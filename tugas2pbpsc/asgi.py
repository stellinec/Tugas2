"""
ASGI config for stelline tugas2pbpsc.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangotugas2pbpsc.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tugas2pbpsc.settings')

application = get_asgi_application()
