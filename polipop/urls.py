from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, include, url

# Admin section
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# Our apps
urlpatterns += patterns('popit.views',
    url( r'^$', 'home', name='home' ),
)

# serve media_root files (only works when settings.DEBUG is True)
# https://docs.djangoproject.com/en/1.3/howto/static-files/#django.conf.urls.static.static
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
