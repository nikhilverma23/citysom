from django import forms
from citysom.util import *
from django.forms.widgets import *
from citysom.event.models import *
from django.contrib.admin import widgets 
from citysom.util import FREQUENCY_CHOICES,\
WEEKS_COUNT, ORDINAL_CHOICES, DAYS_OF_WEEK
from tinymce.widgets import TinyMCE

class EventForm(forms.Form):
    """
    Displaying all the event forms
    """
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['date_started'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed'].widget.attrs['class'] = "datepicker"
        self.fields['date_started1'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed1'].widget.attrs['class'] = "datepicker"
        self.fields['date_started2'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed2'].widget.attrs['class'] = "datepicker"
        self.fields['date_started3'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed3'].widget.attrs['class'] = "datepicker"
        self.fields['date_started4'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed4'].widget.attrs['class'] = "datepicker"
        self.fields['date_started5'].widget.attrs['class'] = "datepicker"
        self.fields['date_completed5'].widget.attrs['class'] = "datepicker"
        categories = Category.objects.all()
        self.fields['category'].choices = [(c.pk,c.type) for c in categories]
        self.fields['category'].widget.attrs['class'] = "category_class"
        self.fields['category'].widget.attrs['style'] = "width: 100px"
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
        if not self.fields['category'].choices[0][0] == '':
            self.fields['category'].choices.insert(0, ('','---------' ) )
        self.fields['event_start_hours_1'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_2'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_3'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_4'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_5'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_6'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_7'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_8'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_9'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_10'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_11'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_12'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_13'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_14'].widget.attrs['class'] = "timepicker"
        self.fields['event_start_hours_15'].widget.attrs['class'] = "timepicker"
        
        self.fields['event_end_hours_1'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_2'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_3'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_4'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_5'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_6'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_7'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_8'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_9'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_10'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_11'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_12'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_13'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_14'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours_15'].widget.attrs['class'] = "timepicker"
        
        self.fields['frequency'].widget.attrs['class'] = "frequency_class"
        self.fields['frequency1'].widget.attrs['class'] = "frequency_class"
        self.fields['frequency2'].widget.attrs['class'] = "frequency_class"
        self.fields['frequency3'].widget.attrs['class'] = "frequency_class"
        self.fields['frequency4'].widget.attrs['class'] = "frequency_class"
        
    title = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'placeholder': 'Your event title'}))
    
    venue_name = forms.CharField(max_length=255,required=False, widget=forms.TextInput(attrs={'placeholder': 'Venue name (optional)'}))
    
    street_address = forms.CharField(max_length=255,required=True, widget=forms.TextInput(attrs={'placeholder': 'The address of the event'}))
    
    date_started = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_completed = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_started1 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_completed1 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    
    date_started2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_completed2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_started3 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_completed3 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_started4 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    date_completed4 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    
    date_started5 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))#

    date_completed5 = forms.DateField(required=False, widget=forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}))

        
    event_duration = forms.DateField(required=False)
 
    event_poster = forms.CharField(required=True)
    
    event_ticket_price = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    
    event_ticket_price_1 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    
    event_ticket_price_2 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    
    event_ticket_price_3 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    
    event_ticket_price_4 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    
    event_ticket_price_5 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    
    event_ticket_price_6 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_7 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_8 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_9 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_10 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_11 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_12 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_13 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_14 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    event_ticket_price_15 = forms.DecimalField(label="Price of a full-price ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g 20 for $20'})
                                    )
    eventwebsite = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'www.'}))
    keyword = forms.CharField(max_length=255,required=False)
    status = forms.BooleanField(required=False,
                                initial=True)
    description = forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':15, 'placeholder':'Let us know more about this great event!'}),required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),\
                                        required=False,
                                        #widget=RadioSelect(),
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
    start_hours_on_monday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_monday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_hours_on_tuesday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_tuesday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_hours_on_wednesday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_wednesday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_hours_on_thursday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_thursday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_hours_on_friday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_friday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_hours_on_saturday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_saturday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_hours_on_sunday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    end_hours_on_sunday = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))

    frequency = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=True,
                                  help_text="weekly,monthly etc"
                                  )
    interval = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    ordinal = forms.ChoiceField(label='',
                                choices=ORDINAL_CHOICES,
                                widget=forms.Select(),
                                required=False,
                                help_text="Ordinal value for monthly repetitions")
    
    ordinal_day = forms.ChoiceField(label='',
                                    choices=DAYS_OF_WEEK,
                                    widget=forms.Select(),
                                    required=False,
                                    help_text="Weekday of repetition for monthly recurrences")
    
    # For PerformanceRepeat 2
    frequency1 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="weekly,monthly etc"
                                  )
    interval1 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on1 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    ordinal1 = forms.ChoiceField(label='',
                                choices=ORDINAL_CHOICES,
                                widget=forms.Select(),
                                required=False,
                                help_text="Ordinal value for monthly repetitions")
    
    ordinal_day1 = forms.ChoiceField(label='',
                                    choices=DAYS_OF_WEEK,
                                    widget=forms.Select(),
                                    required=False,
                                    help_text="Weekday of repetition for monthly recurrences")
    
    # For Performace Repeat 2
    frequency2 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="weekly,monthly etc"
                                  )
    interval2 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on2 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    ordinal2 = forms.ChoiceField(label='',
                                choices=ORDINAL_CHOICES,
                                widget=forms.Select(),
                                required=False,
                                help_text="Ordinal value for monthly repetitions")
    
    ordinal_day2 = forms.ChoiceField(label='',
                                    choices=DAYS_OF_WEEK,
                                    widget=forms.Select(),
                                    required=False,
                                    help_text="Weekday of repetition for monthly recurrences")

    # For Performance Repeat 3
    frequency3 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="weekly,monthly etc"
                                  )
    interval3 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on3 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    ordinal3 = forms.ChoiceField(label='',
                                choices=ORDINAL_CHOICES,
                                widget=forms.Select(),
                                required=False,
                                help_text="Ordinal value for monthly repetitions")
    
    ordinal_day3 = forms.ChoiceField(label='',
                                    choices=DAYS_OF_WEEK,
                                    widget=forms.Select(),
                                    required=False,
                                    help_text="Weekday of repetition for monthly recurrences")

    # Performance Repeat4
    frequency4 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="weekly,monthly etc"
                                  )
    interval4 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on4 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    ordinal4 = forms.ChoiceField(label='',
                                choices=ORDINAL_CHOICES,
                                widget=forms.Select(),
                                required=False,
                                help_text="Ordinal value for monthly repetitions")
    
    ordinal_day4 = forms.ChoiceField(label='',
                                    choices=DAYS_OF_WEEK,
                                    widget=forms.Select(),
                                    required=False,
                                    help_text="Weekday of repetition for monthly recurrences")


    event_start_hours_1 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_2 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_3 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_4 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_5 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_6 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_7 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_8 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_9 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_10 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_11 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_12 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_12 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_13 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_14 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_start_hours_15 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    
    event_end_hours_1 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_2 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_3 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_4 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_5 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_6 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_7 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_8 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_9 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_10 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_11 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_12 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_13 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_14 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    event_end_hours_15 = forms.TimeField(required=False, widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    
    
    
    
    schedule_type = forms.CharField(max_length=40,widget=RadioSelect(choices=SCHEDULE_TYPE),
                                    required=False)
    
    
class EventPosterForm(forms.Form):
     event_poster_file = forms.ImageField(required=False)
     

class EventRatingForm(forms.Form):
    title = forms.CharField(max_length=1024, required=True, error_messages={'required': 'Title is required'})
    ratings = forms.IntegerField(required=True, error_messages={'required': 'Ratings is required'})
    reviews = forms.CharField(widget=forms.Textarea, required=True, error_messages={'required': 'Reviews is required'})