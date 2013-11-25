from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'telDirMgmt.views.home', name='home'),
    url(r'^Directories/', include('Directories.urls', namespace="Directories")),
    url(r'^admin/', include(admin.site.urls)),
)
