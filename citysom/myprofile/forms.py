from django import forms
from django.db import models
from django.forms import ModelForm
from myprofile.models import UserProfile
from django.contrib.admin import widgets 
from citysom.registration.forms import RegistrationForm
from citysom.util import ACCOUNT_TYPE, GENDER_CHOICES
from django.forms.widgets import *
from django.contrib.auth.hashers import PBKDF2PasswordHasher as hasher


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
    gender = forms.ChoiceField(label='Gender',\
                               choices=GENDER_CHOICES,\
                               widget=forms.Select()
                             )
    mobile = forms.CharField(max_length=20,required=False)
    email2 = forms.EmailField(required=False)
    email3 = forms.EmailField(required=False)
    email4 = forms.EmailField(required=False)
    facebook_account = forms.URLField(required=False)
    
class ProfessionalProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProfessionalProfileForm, self).__init__(*args, **kwargs)
        self.fields['start_hours_on_monday'].widget.attrs['class'] = "timepicker monday"
        self.fields['end_hours_on_monday'].widget.attrs['class'] = "timepicker monday"
        self.fields['start_hours_on_tuesday'].widget.attrs['class'] = "timepicker tuesday"
        self.fields['end_hours_on_tuesday'].widget.attrs['class'] = "timepicker tuesday"
        self.fields['start_hours_on_wednesday'].widget.attrs['class'] = "timepicker wednesday"
        self.fields['end_hours_on_wednesday'].widget.attrs['class'] = "timepicker wednesday"
        self.fields['start_hours_on_thursday'].widget.attrs['class'] = "timepicker thursday"
        self.fields['end_hours_on_thursday'].widget.attrs['class'] = "timepicker thursday"
        self.fields['start_hours_on_friday'].widget.attrs['class'] = "timepicker friday"
        self.fields['end_hours_on_friday'].widget.attrs['class'] = "timepicker friday"
        self.fields['start_hours_on_saturday'].widget.attrs['class'] = "timepicker saturday"
        self.fields['end_hours_on_saturday'].widget.attrs['class'] = "timepicker saturday"
        self.fields['start_hours_on_sunday'].widget.attrs['class'] = "timepicker sunday"
        self.fields['end_hours_on_sunday'].widget.attrs['class'] = "timepicker sunday"
       
        
    first_name = forms.CharField(max_length=80,required=False)
    last_name = forms.CharField(max_length=80,required=False)
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES,widget=forms.Select())
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
    
class AccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), label="Password",required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password",required=True)
    
    def clean_password(self):
        if self.cleaned_data.get('password')!= self.data.get('confirm_password'):
            raise forms.ValidationError,'Password does not match'
        return self.cleaned_data['password']
