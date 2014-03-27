from django.conf.urls import patterns, include, url
from django.conf      import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'media/(?P<path>.*)', 'django.views.static.serve', {
        'document_root' : settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += patterns('django.views.static',
#                         url(r'media/(?P<path>.*)', 'serve', {
#                             'document_root' : settings.MEDIA_ROOT }), )
