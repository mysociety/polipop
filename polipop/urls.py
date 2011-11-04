#from django.conf import settings
#from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Project page
    url( r'^$', TemplateView.as_view(template_name='index.html'), name='home' ),

    # Our apps
    ( r'^popit/', include('popit.urls') ),
)

# serve media_root files (only works when settings.DEBUG is True)
# https://docs.djangoproject.com/en/1.3/howto/static-files/#django.conf.urls.static.static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
