#!/usr/bin/env python
import os
import sys
import django
import os
import sys
from django.core.wsgi import get_wsgi_application

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moocOnline.settings")
    django.setup()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    application = get_wsgi_application()