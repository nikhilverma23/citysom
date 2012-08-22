from django import forms
from citysom.util import *
from django.forms.widgets import *
from citysom.event.models import *
from django.contrib.admin import widgets 
from citysom.util import *
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
        
        self.fields['start_hours_on_monday_option1'].widget.attrs['class'] = "timepicker monday1"
        self.fields['end_hours_on_monday_option1'].widget.attrs['class'] = "timepicker monday1"
        self.fields['start_hours_on_tuesday_option1'].widget.attrs['class'] = "timepicker tuesday1"
        self.fields['end_hours_on_tuesday_option1'].widget.attrs['class'] = "timepicker tuesday1"
        self.fields['start_hours_on_wednesday_option1'].widget.attrs['class'] = "timepicker wednesday1"
        self.fields['end_hours_on_wednesday_option1'].widget.attrs['class'] = "timepicker wednesday1"
        self.fields['start_hours_on_thursday_option1'].widget.attrs['class'] = "timepicker thursday1"
        self.fields['end_hours_on_thursday_option1'].widget.attrs['class'] = "timepicker thursday1"
        self.fields['start_hours_on_friday_option1'].widget.attrs['class'] = "timepicker friday1"
        self.fields['end_hours_on_friday_option1'].widget.attrs['class'] = "timepicker friday1"
        self.fields['start_hours_on_saturday_option1'].widget.attrs['class'] = "timepicker saturday1"
        self.fields['end_hours_on_saturday_option1'].widget.attrs['class'] = "timepicker saturday1"
        self.fields['start_hours_on_sunday_option1'].widget.attrs['class'] = "timepicker sunday1"
        self.fields['end_hours_on_sunday_option1'].widget.attrs['class'] = "timepicker sunday1"
        
        self.fields['start_hours_on_monday_option2'].widget.attrs['class'] = "timepicker monday2"
        self.fields['end_hours_on_monday_option2'].widget.attrs['class'] = "timepicker monday2"
        self.fields['start_hours_on_tuesday_option2'].widget.attrs['class'] = "timepicker tuesday2"
        self.fields['end_hours_on_tuesday_option2'].widget.attrs['class'] = "timepicker tuesday2"
        self.fields['start_hours_on_wednesday_option2'].widget.attrs['class'] = "timepicker wednesday2"
        self.fields['end_hours_on_wednesday_option2'].widget.attrs['class'] = "timepicker wednesday2"
        self.fields['start_hours_on_thursday_option2'].widget.attrs['class'] = "timepicker thursday2"
        self.fields['end_hours_on_thursday_option2'].widget.attrs['class'] = "timepicker thursday2"
        self.fields['start_hours_on_friday_option2'].widget.attrs['class'] = "timepicker friday2"
        self.fields['end_hours_on_friday_option2'].widget.attrs['class'] = "timepicker friday2"
        self.fields['start_hours_on_saturday_option2'].widget.attrs['class'] = "timepicker saturday2"
        self.fields['end_hours_on_saturday_option2'].widget.attrs['class'] = "timepicker saturday2"
        self.fields['start_hours_on_sunday_option2'].widget.attrs['class'] = "timepicker sunday2"
        self.fields['end_hours_on_sunday_option2'].widget.attrs['class'] = "timepicker sunday2"
        
        self.fields['start_hours_on_monday_option3'].widget.attrs['class'] = "timepicker monday3"
        self.fields['end_hours_on_monday_option3'].widget.attrs['class'] = "timepicker monday3"
        self.fields['start_hours_on_tuesday_option3'].widget.attrs['class'] = "timepicker tuesday3"
        self.fields['end_hours_on_tuesday_option3'].widget.attrs['class'] = "timepicker tuesday3"
        self.fields['start_hours_on_wednesday_option3'].widget.attrs['class'] = "timepicker wednesday3"
        self.fields['end_hours_on_wednesday_option3'].widget.attrs['class'] = "timepicker wednesday3"
        self.fields['start_hours_on_thursday_option3'].widget.attrs['class'] = "timepicker thursday3"
        self.fields['end_hours_on_thursday_option3'].widget.attrs['class'] = "timepicker thursday3"
        self.fields['start_hours_on_friday_option3'].widget.attrs['class'] = "timepicker friday3"
        self.fields['end_hours_on_friday_option3'].widget.attrs['class'] = "timepicker friday3"
        self.fields['start_hours_on_saturday_option3'].widget.attrs['class'] = "timepicker saturday3"
        self.fields['end_hours_on_saturday_option3'].widget.attrs['class'] = "timepicker saturday3"
        self.fields['start_hours_on_sunday_option3'].widget.attrs['class'] = "timepicker sunday3"
        self.fields['end_hours_on_sunday_option3'].widget.attrs['class'] = "timepicker sunday3"
        #if not self.fields['category'].choices[0][0] == '':
        #    self.fields['category'].choices.insert(0, ('','---------' ) )
        self.fields['event_start_hours'].widget.attrs['class'] = "timepicker"
        self.fields['event_end_hours'].widget.attrs['class'] = "timepicker"
        self.fields['schedule_type'].widget.attrs['class'] = "schedule_class"
        self.fields['schedule_type_option1'].widget.attrs['class'] = "schedule_class"
        self.fields['schedule_type_option2'].widget.attrs['class'] = "schedule_class"
        self.fields['schedule_type_option3'].widget.attrs['class'] = "schedule_class"
        
    title = forms.CharField(max_length=255,required=True)
    venue_name = forms.CharField(max_length=255,required=False)
    street_address = forms.CharField(max_length=255,required=True)
    
    date_started = forms.DateField(required=True)
    date_completed = forms.DateField(required=True)
    schedule_type = forms.CharField(max_length=40,widget=RadioSelect(choices=SCHEDULE_TYPE),
                                    required=False)
    
    ################################################
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
    ########################################################
    
    
    
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
    event_start_hours = forms.TimeField(required=False)
    event_end_hours = forms.TimeField(required=False)
    
    repeat_on = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    by_set_pos = forms.ChoiceField(label="By Set Pos",\
                                  choices=SET_POS_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="first,second,...last"
                                  )
    byweekday = forms.ChoiceField(label="Repeat on the",
                                 choices=DAYS_OF_WEEK_SHORT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="Monday, Tuesday"
                                )
    event_ticket_price = forms.DecimalField(label="Price Full Ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False
                                    )
    
    # Replicating because of creating formsets
    
    date_started_option1 = forms.DateField(required=True)
    date_completed_option1 = forms.DateField(required=True)
    schedule_type_option1 = forms.CharField(max_length=40,widget=RadioSelect(choices=SCHEDULE_TYPE),
                                    required=False)
    # if open hour based
    start_hours_on_monday_option1 = forms.TimeField(required=False)
    end_hours_on_monday_option1 = forms.TimeField(required=False)
    start_hours_on_tuesday_option1 = forms.TimeField(required=False)
    end_hours_on_tuesday_option1 = forms.TimeField(required=False)
    start_hours_on_wednesday_option1 = forms.TimeField(required=False)
    end_hours_on_wednesday_option1 = forms.TimeField(required=False)
    start_hours_on_thursday_option1 = forms.TimeField(required=False)
    end_hours_on_thursday_option1 = forms.TimeField(required=False)
    start_hours_on_friday_option1 = forms.TimeField(required=False)
    end_hours_on_friday_option1 = forms.TimeField(required=False)
    start_hours_on_saturday_option1 = forms.TimeField(required=False)
    end_hours_on_saturday_option1 = forms.TimeField(required=False)
    start_hours_on_sunday_option1 = forms.TimeField(required=False)
    end_hours_on_sunday_option1 = forms.TimeField(required=False)
    
    # if performance based
    frequency_option1 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=True,
                                  help_text="weekly,monthly etc"
                                  )
    interval_option1 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on_option1 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    by_set_pos_option1 = forms.ChoiceField(label="By Set Pos",\
                                  choices=SET_POS_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="first,second,...last"
                                  )
    byweekday_option1 = forms.ChoiceField(label="Repeat on the",
                                 choices=DAYS_OF_WEEK_SHORT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="Monday, Tuesday"
                                )
    event_ticket_price_option1 = forms.DecimalField(label="Price Full Ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False
                                    )
    
   
    event_start_hours_option1 = forms.TimeField(required=False)
    event_end_hours_option1 = forms.TimeField(required=False)
    
    
    
    # Replicating because of creating formsets
    
    date_started_option2 = forms.DateField(required=True)
    date_completed_option2 = forms.DateField(required=True)
    schedule_type_option2 = forms.CharField(max_length=40,widget=RadioSelect(choices=SCHEDULE_TYPE),
                                    required=False)
    
    # if open hour based
    start_hours_on_monday_option2 = forms.TimeField(required=False)
    end_hours_on_monday_option2 = forms.TimeField(required=False)
    start_hours_on_tuesday_option2 = forms.TimeField(required=False)
    end_hours_on_tuesday_option2 = forms.TimeField(required=False)
    start_hours_on_wednesday_option2 = forms.TimeField(required=False)
    end_hours_on_wednesday_option2 = forms.TimeField(required=False)
    start_hours_on_thursday_option2 = forms.TimeField(required=False)
    end_hours_on_thursday_option2 = forms.TimeField(required=False)
    start_hours_on_friday_option2 = forms.TimeField(required=False)
    end_hours_on_friday_option2 = forms.TimeField(required=False)
    start_hours_on_saturday_option2 = forms.TimeField(required=False)
    end_hours_on_saturday_option2 = forms.TimeField(required=False)
    start_hours_on_sunday_option2 = forms.TimeField(required=False)
    end_hours_on_sunday_option2 = forms.TimeField(required=False)
    
    # if performance based
    frequency_option2 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=True,
                                  help_text="weekly,monthly etc"
                                  )
    interval_option2 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on_option2 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    by_set_pos_option2 = forms.ChoiceField(label="By Set Pos",\
                                  choices=SET_POS_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="first,second,...last"
                                  )
    byweekday_option2 = forms.ChoiceField(label="Repeat on the",
                                 choices=DAYS_OF_WEEK_SHORT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="Monday, Tuesday"
                                )
    event_ticket_price_option2 = forms.DecimalField(label="Price Full Ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False
                                    )
    
   
    event_start_hours_option2 = forms.TimeField(required=False)
    event_end_hours_option2 = forms.TimeField(required=False)
    
    
    
    # Replicating because of creating formsets
    date_started_option3 = forms.DateField(required=True)
    date_completed_option3 = forms.DateField(required=True)
    schedule_type_option3 = forms.CharField(max_length=40,widget=RadioSelect(choices=SCHEDULE_TYPE),
                                    required=False)
    # if open hour based
    start_hours_on_monday_option3 = forms.TimeField(required=False)
    end_hours_on_monday_option3 = forms.TimeField(required=False)
    start_hours_on_tuesday_option3 = forms.TimeField(required=False)
    end_hours_on_tuesday_option3 = forms.TimeField(required=False)
    start_hours_on_wednesday_option3 = forms.TimeField(required=False)
    end_hours_on_wednesday_option3 = forms.TimeField(required=False)
    start_hours_on_thursday_option3 = forms.TimeField(required=False)
    end_hours_on_thursday_option3 = forms.TimeField(required=False)
    start_hours_on_friday_option3 = forms.TimeField(required=False)
    end_hours_on_friday_option3 = forms.TimeField(required=False)
    start_hours_on_saturday_option3 = forms.TimeField(required=False)
    end_hours_on_saturday_option3 = forms.TimeField(required=False)
    start_hours_on_sunday_option3 = forms.TimeField(required=False)
    end_hours_on_sunday_option3 = forms.TimeField(required=False)
    
    # if performance based
    frequency_option3 = forms.ChoiceField(label="Events Repeats",\
                                  choices=FREQUENCY_CHOICES,\
                                  widget=forms.Select(),\
                                  required=True,
                                  help_text="weekly,monthly etc"
                                  )
    interval_option3 = forms.ChoiceField(label="Repeat Every",
                                 choices=WEEKS_COUNT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="basically the count"
                                )
    repeat_on_option3 = forms.ModelMultipleChoiceField(
                        queryset = Days.objects.all(),                          
                        widget=CheckboxSelectMultiple,
                        required=False,
                        initial = "Event Repeats"
                        )
    by_set_pos_option3 = forms.ChoiceField(label="By Set Pos",\
                                  choices=SET_POS_CHOICES,\
                                  widget=forms.Select(),\
                                  required=False,
                                  help_text="first,second,...last"
                                  )
    byweekday_option3 = forms.ChoiceField(label="Repeat on the",
                                 choices=DAYS_OF_WEEK_SHORT,
                                 widget=forms.Select(),\
                                 required=False,
                                 help_text="Monday, Tuesday"
                                )
    event_ticket_price_option3 = forms.DecimalField(label="Price Full Ticket",\
                                    max_digits=12,\
                                    decimal_places=2,
                                    required=False
                                    )
    
   
    event_start_hours_option3 = forms.TimeField(required=False)
    event_end_hours_option3 = forms.TimeField(required=False)
    
    ##############################################################
    event_duration = forms.DateField(required=False)
    event_poster = forms.CharField(required=False)
    eventwebsite = forms.URLField(required=False)
    keyword = forms.CharField(max_length=255,required=False)
    status = forms.BooleanField(required=False,
                                initial=True)
    description = forms.CharField(max_length=255,required=False)
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
    
    
    

    
    

    
    
    
    
class EventPosterForm(forms.Form):
     event_poster_file = forms.ImageField(required=False)
     


      
