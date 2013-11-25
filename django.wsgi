import os
import sys

path='/home/petran/Django/telDirMgmt'

if path not in sys.path:
 sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'telDirMgmt.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
