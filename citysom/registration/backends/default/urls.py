"""
URLconf for registration and activation, using django-registration's
default backend.

If the default behavior of these views is acceptable to you, simply
use a line like this in your root URLconf to set up the default URLs
for registration::

    (r'^accounts/', include('registration.backends.default.urls')),

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""


from django.conf.urls.defaults import *
from django.contrib.auth.models import Group
from django.views.generic.simple import direct_to_template
from citysom.registration.forms import RegistrationFormUniqueEmail
from citysom.registration.forms import RegistrationForm
from citysom.myprofile.forms import UserProfileForm, PreRegistrationForm
from citysom.registration.views import activate
from citysom.registration.views import register
import citysom.settings
import citysom.myprofile.regbackened



urlpatterns = patterns('',
                       url(r'^activate/complete/$',
                           direct_to_template,
                           {'template': 'registration/activation_complete.html',
                            'extra_context': {'profile_form': UserProfileForm,
                                              'expiration_days':citysom.settings.ACCOUNT_ACTIVATION_DAYS}},
                           name='registration_activation_complete'),
                       
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate/(?P<activation_key>\w+)/$',
                           activate,
                           {'backend': 'registration.backends.default.DefaultBackend',
                            #'success_url': '/myprofile/completingprofile/',
                            'success_url': '/myprofile/get_account_type/',
                                                   
                            'template_name':'registration/activation_failed.html'},
                           name='registration_activate'),
                       
                       url(r'^register/$',
                           register,
                           {'backend': 'registration.backends.default.DefaultBackend',
                            'form_class':RegistrationFormUniqueEmail,
                            'success_url':'/accounts/register/complete/'},
                           name='registration_register'),
                       
                       url(r'^register/complete/$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html',
                            'extra_context': {'expiration_days':citysom.settings.ACCOUNT_ACTIVATION_DAYS}},
                           name='registration_complete'),
                       url(r'^register/closed/$',
                           direct_to_template,
                           { 'template': 'registration/registration_closed.html' },
                           name='registration_disallowed'),
                       (r'', include('citysom.registration.auth_urls')),
                       
                                     
                       )
