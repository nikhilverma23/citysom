from django.conf.urls.defaults import *
from citysom.event.views import eventcreation

urlpatterns = patterns(
    "citysom.event.views",
    
    (r'^createevent/$', 'eventcreation'),
    (r'^upload_image/$', 'handle_uploaded_file'),
    (r'^event_list/$', 'event_list'),
    (r'^event_genre/$', 'get_event_genre'),
    (r'^calendar/$', 'calendar')
)