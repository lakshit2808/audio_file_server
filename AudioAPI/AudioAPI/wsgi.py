"""
WSGI config for AudioAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

path = '/home/path/to/project'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AudioAPI.settings')

application = get_wsgi_application()

