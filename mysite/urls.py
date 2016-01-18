from django.conf.urls.defaults import *
import os.path
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'mysite.views.index'),
    (r'^medias/css/default', 'mysite.views.default'),
    (r'^medias/js/jquery', 'mysite.views.jquery'),
    (r'^medias/js/garden', 'mysite.views.garden'),
    (r'^medias/js/functions','mysite.views.functions'),
)

#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)