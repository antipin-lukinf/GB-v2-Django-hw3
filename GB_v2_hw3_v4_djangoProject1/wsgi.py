"""
WSGI config for GB_v2_hw3_v4_djangoProject1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GB_v2_hw3_v4_djangoProject1.settings')

application = get_wsgi_application()
