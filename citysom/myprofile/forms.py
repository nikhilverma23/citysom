from django import forms
from django.db import models
from django.forms import ModelForm
from myprofile.models import UserProfile
from django.contrib.admin import widgets 
from citysom.registration.forms import RegistrationForm
from citysom.util import ACCOUNT_TYPE, GENDER_CHOICES
from django.forms.widgets import *


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','account_type')
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        


class EditUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        
        
        
class PreRegistrationForm(forms.Form):
    account_type = forms.BooleanField(label="Personal Account",\
                                          required=True,
                                          widget = RadioSelect(choices=ACCOUNT_TYPE)
                                          )
    

class PersonalProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name",max_length=80)
    last_name = forms.CharField(label="Last Name",max_length=80,required=False)
    gender = forms.CharField(label="Gender",max_length=20,\
                             widget=Select(choices=GENDER_CHOICES)
                             )
    mobile = forms.CharField(max_length=20,required=False)
    email2 = forms.EmailField(required=False)
    email3 = forms.EmailField(required=False)
    email4 = forms.EmailField(required=False)
    facebook_account = forms.URLField()
    
class ProfessionalProfileForm(forms.Form):
    first_name = forms.CharField(max_length=80,required=False)
    last_name = forms.CharField(max_length=80,required=False)
    gender = forms.CharField(max_length=20,widget=Select(choices=GENDER_CHOICES))
    mobile = forms.CharField(max_length=80,required=False)
    institution_name = forms.CharField(max_length=80,required=False)
    street = forms.CharField(max_length=80,required=False)
    zip_code = forms.CharField(max_length=80,required=False)
    state = forms.CharField(max_length=80,required=False)
    country = forms.CharField(max_length=80,required=False)
    institution_website = forms.URLField(required=False)
    start_hours_on_monday = forms.TimeField(label="Monday",required=False)
    end_hours_on_monday = forms.TimeField(label="",required=False)
    start_hours_on_tuesday = forms.TimeField(label="Tuesday",required=False)
    end_hours_on_tuesday = forms.TimeField(label="",required=False)
    start_hours_on_wednesday = forms.TimeField(label="Wednesday",required=False)
    end_hours_on_wednesday = forms.TimeField(label="",required=False)
    start_hours_on_thursday = forms.TimeField(label="Thursday",required=False)
    end_hours_on_thursday = forms.TimeField(label="",required=False)
    start_hours_on_friday = forms.TimeField(label="Friday",required=False)
    end_hours_on_friday = forms.TimeField(label="",required=False)
    start_hours_on_saturday = forms.TimeField(label="Saturday",required=False)
    end_hours_on_saturday = forms.TimeField(label="",required=False)
    start_hours_on_sunday = forms.TimeField(label="Sunday",required=False)
    end_hours_on_sunday = forms.TimeField(label="",required=False)
    
    