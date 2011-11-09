from django.shortcuts  import render, get_object_or_404, redirect
from django.views.generic import ListView

# from django.views.generic.list_detail import object_detail, object_list

from popit import models

class PositionTypeListView(ListView):
    context_object_name = 'position_list'

    def get_queryset(self):
        type = get_object_or_404(models.PositionType, self.args[0])
        return Position.objects.filter(type=type)

