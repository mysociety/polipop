#!/usr/bin/python 

import os, sys

paths = (
    '../polipop',
    '../',
    '../pylib/',
    '../commonlib/pylib/',
)
file_dir = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
for path in paths:
    abspath = os.path.normpath(os.path.join(file_dir, path))
    if abspath not in sys.path:
        sys.path.insert(0, abspath)

import mysociety.config
mysociety.config.set_file(os.path.abspath(file_dir + "/../conf/general"))

if mysociety.config.get('STAGING'):
    import wsgi_monitor
    wsgi_monitor.start(interval=1.0)
    # wsgi_monitor.track(os.path.join(os.path.dirname(__file__), 'site.cf'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'polipop.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
