from django.conf.urls.defaults import *
from citysom.event.views import eventcreation

urlpatterns = patterns(
    "citysom.event.views",
    
    (r'^createevent/$', 'eventcreation'),
    (r'^upload_image/$', 'handle_uploaded_file'),
    (r'^event_list/$', 'event_list'),
    (r'^event_genre/$', 'get_event_genre'),
    (r'^calendar/$', 'calendar'),
    (r'^details/$', 'get_event_details'),
    (r'^update_city/$', 'update_city'),
    (r'^comment_delete/$', 'comment_delete'),
    url(r'^export/$', 'export', name="event_export"),
)