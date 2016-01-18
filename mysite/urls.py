from django.conf.urls.defaults import *
import os.path
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
    (r'^med/$', 'mysite.views.med'),
    (r'^alg/$', 'mysite.views.alg'),
    (r'^demo/$', 'mysite.demo.views.showdemo'),
    (r'^site_medias/(?P<path>.*)$','django.views.static.serve',
)
