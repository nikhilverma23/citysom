from datetime import datetime
import logging
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db  import models
from citysom.util import EVENT_GENRE, EVENT_PUBLIC,\
DAYS_OF_WEEK 


class Place(models.Model):
    """
    where the event is taking place
    """
    venue_name = models.CharField(max_length=255)
    # event  start hours on respective weekdays
    institution_name = models.CharField(max_length=100,blank=True,null=True)
    institution_website = models.CharField(max_length=100,blank=True,null=True)
    street = models.CharField(max_length=255)
    state = models.CharField(max_length=30)
    zip_code = models.IntegerField(max_length=7, blank=True, null=True)
    start_hours_on_monday = models.TimeField(null=True,blank=True)
    end_hours_on_monday = models.TimeField(null=True,blank=True)
    start_hours_on_tuesday = models.TimeField(null=True,blank=True)
    end_hours_on_tuesday = models.TimeField(null=True,blank=True)
    start_hours_on_wednesday = models.TimeField(null=True,blank=True)
    end_hours_on_wednesday = models.TimeField(null=True,blank=True)
    start_hours_on_thursday = models.TimeField(null=True,blank=True)
    end_hours_on_thursday = models.TimeField(null=True,blank=True)
    start_hours_on_friday = models.TimeField(null=True,blank=True)
    end_hours_on_friday = models.TimeField(null=True,blank=True)
    start_hours_on_saturday = models.TimeField(null=True,blank=True)
    end_hours_on_saturday = models.TimeField(null=True,blank=True)
    start_hours_on_sunday = models.TimeField(null=True,blank=True)
    end_hours_on_sunday = models.TimeField(null=True,blank=True) 
    
    
    def __unicode__(self):
        return self.venue_name



class Category(models.Model):
    """
    Describes the Event Category
    """
    type = models.CharField(max_length=20,\
                                  help_text = "type of event"
                                  )

    def __unicode__(self):
        return self.type  


class EventGenre(models.Model):
    """
    Describes the various genre
    """
    category = models.ForeignKey(Category, null=True, blank=True)
    genre_choices = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.genre_choices
        
class EventPublic(models.Model):
    """
    Describes the audience who watch the event
    """
    choicelist = models.CharField(max_length=255)
    
    
    def __unicode__(self):
        return self.choicelist
    

class Days(models.Model):
    week_day = models.CharField(max_length=20,null=True,blank=True)
    
    def __unicode__(self):
        return self.week_day

    
class Event(models.Model):
    """
    Charactersitics of Event
    """
    
   
    # Name of event
    title = models.CharField(max_length=200)
    # Event Website
    eventwebsite = models.URLField(max_length=255,blank=True,null=True)
    
    description = models.TextField(blank=True,null=True)
    
    keyword = models.CharField(max_length=25,null=True,blank=True)
    # Where the event is taking place
    location = models.ForeignKey(Place,blank=True,null=True)
    # What type of event is this.
    category = models.ForeignKey(Category)
    # Who sets up the event
    user = models.ForeignKey(User,db_column="event_created_by",\
                             related_name="who_sets_the_event",\
                             help_text="Who sets the event")
    
    status = models.BooleanField(default=False,\
                                 help_text="Event is active or Inactive")
    # Image for Event
    event_poster = models.ImageField(upload_to="images/",\
                                     max_length=100,blank=True,null=True)
    
    # Any videos of event
    video = models.FileField(upload_to="videos/",blank=True,null=True,\
                             help_text="Video of Event if any(to be added later)")
    
    event_genre = models.ManyToManyField(EventGenre,blank=True,null=True)
    
    # audience for this event like adults ,children etc
    event_public = models.ManyToManyField(EventPublic,blank=True, null=True)
    schedule_type = models.CharField(max_length=255,blank=True,null=True)
    # For Open Hour Events
    start_hours_on_monday = models.TimeField(null=True,blank=True)
    end_hours_on_monday = models.TimeField(null=True,blank=True)
    start_hours_on_tuesday = models.TimeField(null=True,blank=True)
    end_hours_on_tuesday = models.TimeField(null=True,blank=True)
    start_hours_on_wednesday = models.TimeField(null=True,blank=True)
    end_hours_on_wednesday = models.TimeField(null=True,blank=True)
    start_hours_on_thursday = models.TimeField(null=True,blank=True)
    end_hours_on_thursday = models.TimeField(null=True,blank=True)
    start_hours_on_friday = models.TimeField(null=True,blank=True)
    end_hours_on_friday = models.TimeField(null=True,blank=True)
    start_hours_on_saturday = models.TimeField(null=True,blank=True)
    end_hours_on_saturday = models.TimeField(null=True,blank=True)
    start_hours_on_sunday = models.TimeField(null=True,blank=True)
    end_hours_on_sunday = models.TimeField(null=True,blank=True) 
    # For Performance based Events
    # When the event was started
    event_start_date = models.DateField(help_text="when the event was started"\
                                        ,null=True,\
                                         blank=True
                                         )
    # When the event was completed
    event_completion_date = models.DateField(null=True, blank=True)
    frequency = models.CharField(max_length=80,\
                                 blank=True,null=True,\
                                 help_text="weekly,monthly etc"
                                 )
    
    interval = models.IntegerField(null=True, help_text="basically the count")
    by_day = models.ManyToManyField(Days,\
                                    blank=True,null=True,
                                    help_text="by_day",
                                    )
    by_monthday = models.CharField(max_length=80,blank=True,null=True)
    by_month = models.CharField(max_length=80,blank=True,null=True)

    #Performance Repeat 1
    frequency1 = models.CharField(max_length=80,\
                                 blank=True,null=True,\
                                 help_text="weekly,monthly etc"
                                 )
    
    interval1 = models.IntegerField(null=True, help_text="basically the count")
    by_day1 = models.ManyToManyField(Days,\
                                    db_column = "by_day1",
                                    related_name="event_event_by_day1",
                                    blank=True,null=True,
                                    help_text="by_day1",
                                    )
    by_monthday1 = models.CharField(max_length=80,blank=True,null=True)
    by_month1 = models.CharField(max_length=80,blank=True,null=True)
    #Performance Repeat 2
    frequency2 = models.CharField(max_length=80,\
                             blank=True,null=True,\
                             help_text="weekly,monthly etc"
                             )
    
    interval2 = models.IntegerField(null=True, help_text="basically the count")
    by_day2 = models.ManyToManyField(Days,\
                                    db_column = "by_day2",
                                    related_name="event_event_by_day2",
                                    blank=True,null=True,
                                    help_text="by_day2",
                                    )
    by_monthday2 = models.CharField(max_length=80,blank=True,null=True)
    by_month2 = models.CharField(max_length=80,blank=True,null=True)
    # Performance Repeat 3

    frequency3 = models.CharField(max_length=80,\
                             blank=True,null=True,\
                             help_text="weekly,monthly etc"
                             )
    
    interval3 = models.IntegerField(null=True, help_text="basically the count")
    by_day3 = models.ManyToManyField(Days,\
                                    db_column = "by_day3",
                                    related_name="event_event_by_day3",
                                    blank=True,null=True,
                                    help_text="by_day3",
                                    )
    by_monthday3 = models.CharField(max_length=80,blank=True,null=True)
    by_month3 = models.CharField(max_length=80,blank=True,null=True)
    #Performance Repeat 4
    frequency4 = models.CharField(max_length=80,\
                             blank=True,null=True,\
                             help_text="weekly,monthly etc"
                             )
    
    interval4 = models.IntegerField(null=True, help_text="basically the count")
    by_day4 = models.ManyToManyField(Days,\
                                    db_column = "by_day4",
                                    related_name="event_event_by_day4",
                                    blank=True,null=True,
                                    help_text="by_day4",
                                    )
    by_monthday4 = models.CharField(max_length=80,blank=True,null=True)
    by_month4 = models.CharField(max_length=80,blank=True,null=True)

    
    def duration(self):
        return self.date_started - self.date_completed
    
    def __unicode__(self):
        result =  "Event id:%s, title:%s" %(self.id, self.title)
        return result 




class PerformanceDetails(models.Model):
    """
    Performance parameter
    """
    date_of_performance = models.DateField(help_text="when the event was\
                                           started",\
                                           null=True, blank=True
                                           )
    
    event = models.ForeignKey(Event,null=True,blank=True)
    place = models.ForeignKey(Place,null=True,blank=True)
    showtimes_start = models.TimeField(blank=True,null=True)
    showtimes_end = models.TimeField(blank=True,null=True)
    ticket_price = models.DecimalField(verbose_name="Full Price Ticket",max_digits=8, decimal_places=2, null=True)

    def __unicode__(self):
        showtimes_start = str(self.showtimes_start)
        return showtimes_start
        
class UserComments(models.Model):
    title = models.CharField(max_length=1024,null=True, blank=True)
    ratings = models.IntegerField(null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)
    event = models.ForeignKey(Event, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    status = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title