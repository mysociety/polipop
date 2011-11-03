import os
import time

from django import template
from django.conf import settings

register = template.Library()
version_cache = {}

def version(path_string):
    if settings.DEBUG:
        return '%s?%d' % (path_string, time.time())
    try:
        if path_string in version_cache:
            mtime = version_cache[path_string]
        else:
            mtime = os.path.getmtime( '%s/%s' % (settings.STATIC_ROOT, path_string) )
        return '%s?%d' % (path_string, mtime)
    except:
        return path_string

register.simple_tag(version)

