from django.conf.urls.defaults import *


urlpatterns = patterns(
    "citysom.myprofile.views",
    
    url(r'^completingprofile/$', 'completingprofile', name="profile"),
    (r'^get_account_type/$', 'get_account_type'),
    url(r'^editprofile/$', 'editprofile',  name="editprofile"),
    url(r'^wishlist/$', 'wishlist'),
    url(r'^dashboard/$', 'dashboard',  name="dashboard"),
    url(r'^myevents/$', 'user_events', name="user_events"),
    url(r'^invitation/$', 'invitation',  name="invitation")
)
