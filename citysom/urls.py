from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from citysom.settings import MEDIA_ROOT, STATIC_ROOT
from django.contrib import admin
admin.autodiscover()

handler500 = 'citysom.event.views.server_error'

urlpatterns = patterns('',
    
    
    # for home_page
    url(r'^$', "event.views.splash", name='splash'),
    url(r'^home/',"event.views.home", name='home'),
    (r'^myprofile/home/', 'event.views.home'),

    # for automatic admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^registerfb/$','myprofile.views.registerfb'),
    url(r'^event/details/registerfb/$','myprofile.views.registerfb',name="registerfb"),
    # for event app
    url(r'^myprofile/', include('myprofile.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^about_us/$', direct_to_template, {'template': 'aboutus.html'}, 'about_us'),
    url(r'^contact_us/$', direct_to_template, {'template': 'contactus.html'}, name='contact_us'),
    url(r'^legal_info/$', direct_to_template, {'template': 'legal_info.html'}, name='legal_info'),
    
    #for django-registration app.
    (r'^tinymce/', include('tinymce.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),

      # Static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

