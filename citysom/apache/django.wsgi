"""
WSGI config for citysom project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""


import os, sys
path = '/home/citysom/citysom/'
if path not in sys.path:
    sys.path.append(path)


import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citysom.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


# BEGIN WORKAROUND FOR 500 ERROR WHEN DEBUG=False
#
from django.core.management.validation import get_validation_errors 
try: 
     from cStringIO import StringIO 
except ImportError: 
     from StringIO import StringIO 
s = StringIO() 
num_errors = get_validation_errors(s, None) 

# END WORKAROUND
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
