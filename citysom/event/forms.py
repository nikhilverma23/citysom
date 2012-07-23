from django import forms
from citysom.util import *
from django.forms.widgets import *
from citysom.event.models import *
from django.contrib.admin import widgets 
from citysom.util import FREQUENCY_CHOICES,\
WEEKS_COUNT
from tinymce.widgets import TinyMCE

class EventForm(forms.Form):
    """
    Displaying all the event forms
    """
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['date_started'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed'].widget.attrs['class'] = "datepicker"
        categories = Category.objects.all()
        self.fields['category'].choices = [(c.pk,c.type) for c in categories]
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
        
        
    title = forms.CharField(max_length=255,required=True)
    venue_name = forms.CharField(max_length=255,required=False)
    street_address = forms.CharField(max_length=255,required=True)
    
    date_started = forms.DateField(required=True)

    date_completed = forms.DateField(required=True)

    event_duration = forms.DateField(required=False)
 
    event_poster = forms.CharField(required=False)
    event_ticket_price = forms.DecimalField(label="Price Full Ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False
                                    )
    
    eventwebsite = forms.URLField(required=False)
    keyword = forms.CharField(max_length=255,required=False)
    status = forms.BooleanField(required=False,
                                initial=False)
    description = forms.CharField(max_length=255,required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),\
                                        required=False,
                                        widget=RadioSelect(),
                                        )
    event_genre = forms.ModelMultipleChoiceField(
                        queryset = EventGenre.objects.all(),
                        widget=CheckboxSelectMultiple,
                        required=False
                        )
    event_public = forms.ModelMultipleChoiceField(
                        queryset = EventPublic.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False
                        )
    
    
    
    """
    events starting hours
    """
    start_hours_on_monday = forms.TimeField(required=False)
    end_hours_on_monday = forms.TimeField(required=False)
    start_hours_on_tuesday = forms.TimeField(required=False)
    end_hours_on_tuesday = forms.TimeField(required=False)
    start_hours_on_wednesday = forms.TimeField(required=False)
    end_hours_on_wednesday = forms.TimeField(required=False)
    start_hours_on_thursday = forms.TimeField(required=False)
    end_hours_on_thursday = forms.TimeField(required=False)
    start_hours_on_friday = forms.TimeField(required=False)
    end_hours_on_friday = forms.TimeField(required=False)
    start_hours_on_saturday = forms.TimeField(required=False)
    end_hours_on_saturday = forms.TimeField(required=False)
    start_hours_on_sunday = forms.TimeField(required=False)
    end_hours_on_sunday = forms.TimeField(required=False)

    frequency = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=True,
                                  help_text="weekly,monthly etc"
                                  )
    interval = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=True,
                                 help_text="basically the count"
                                )
    repeat_on = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    schedule_type = forms.CharField(max_length=40,widget=RadioSelect(choices=SCHEDULE_TYPE),
                                    required=False)
    
    
class EventPosterForm(forms.Form):
     event_poster_file = forms.ImageField(required=False)
     


      
