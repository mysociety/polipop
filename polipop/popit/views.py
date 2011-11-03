from django.shortcuts  import render, get_object_or_404, redirect
from django.template   import RequestContext

# from django.views.generic.list_detail import object_detail, object_list

from popit import models

def home(request):
    """Homepage"""
    return render(request, 'index.html')

