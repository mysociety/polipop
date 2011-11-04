from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

# Our apps
urlpatterns = patterns('',
    url( r'^$', TemplateView.as_view(template_name='popit/index.html') ),
)

