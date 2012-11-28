# Create your views here.
import sys
# Python imports
import datetime
import dateutil
import shutil
from dateutil import rrule
from operator import or_, and_
from dateutil.relativedelta import *
from calendar import monthrange
# django  imports
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import http
from django.db.models import Q, Count, Max, Min
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse,HttpResponseRedirect, HttpResponseServerError
# citysom imports
from citysom import settings
from citysom.myprofile.models import History
from citysom.settings import MEDIA_ROOT,STATIC_ROOT
from citysom.event.forms import EventForm, EventPosterForm, EventRatingForm
from citysom.event.models import Place, Event, Category, PerformanceDetails, UserComments, Days

#----------------------------------------------------------------------------#
def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context: sys.exc_info() results
     """
    t = loader.get_template(template_name) 
    ltype,lvalue,ltraceback = sys.exc_info()
    sys.exc_clear() 
    return http.HttpResponseServerError(t.render(Context({'type':ltype,'value':lvalue,'traceback':ltraceback})))

#----------------------------------------------------------------------------#
def eventcreation(request):
    if request.method == "POST":
        event_form = EventForm(request.POST,request.FILES) 
        eventposter_form = EventPosterForm(request.POST,request.FILES)
        if event_form.is_valid():
            try:
                id = request.GET['id']
                old_event_obj = Event.objects.get(id=id)
                
                if old_event_obj.event_poster:
                    event_poster = old_event_obj.event_poster
            except:
                pass
            
            if event_form.cleaned_data['event_poster']:
                event_poster = event_form.cleaned_data['event_poster']
            
            place_obj, created = Place.objects.get_or_create(
                                                             venue_name = event_form.cleaned_data['venue_name'],
                                                             street = event_form.cleaned_data['street_address'],
                                                             start_hours_on_monday = event_form.cleaned_data['start_hours_on_monday'],
                                                             end_hours_on_monday = event_form.cleaned_data['end_hours_on_monday'],
                                                             start_hours_on_tuesday = event_form.cleaned_data['start_hours_on_tuesday'],
                                                             end_hours_on_tuesday = event_form.cleaned_data['end_hours_on_monday'],
                                                             start_hours_on_wednesday = event_form.cleaned_data['start_hours_on_wednesday'],
                                                             end_hours_on_wednesday = event_form.cleaned_data['end_hours_on_wednesday'],
                                                             start_hours_on_thursday = event_form.cleaned_data['start_hours_on_thursday'],
                                                             end_hours_on_thursday = event_form.cleaned_data['end_hours_on_thursday'],
                                                             start_hours_on_friday = event_form.cleaned_data['start_hours_on_friday'],
                                                             end_hours_on_friday = event_form.cleaned_data['end_hours_on_friday'],
                                                             start_hours_on_saturday = event_form.cleaned_data['start_hours_on_saturday'],
                                                             end_hours_on_saturday = event_form.cleaned_data['end_hours_on_saturday'],
                                                             start_hours_on_sunday = event_form.cleaned_data['start_hours_on_sunday'],
                                                             end_hours_on_sunday = event_form.cleaned_data['end_hours_on_sunday'],
                                                             )
                       
            
            event_obj, created = Event.objects.get_or_create(
                                                             user = request.user,
                                                             title = event_form.cleaned_data['title'],            
                                                             eventwebsite = event_form.cleaned_data['eventwebsite'],
                                                             keyword = event_form.cleaned_data['keyword'],
                                                             description = event_form.cleaned_data['description'],
                                                             status = event_form.cleaned_data['status'],
                                                             event_poster = event_poster,
                                                             location = place_obj,
                                                             category = event_form.cleaned_data['category'], 
                                                             schedule_type = event_form.cleaned_data['schedule_type'],
                                                             start_hours_on_monday = event_form.cleaned_data['start_hours_on_monday'],
                                                             end_hours_on_monday = event_form.cleaned_data['end_hours_on_monday'],
                                                             start_hours_on_tuesday = event_form.cleaned_data['start_hours_on_tuesday'],
                                                             end_hours_on_tuesday = event_form.cleaned_data['end_hours_on_monday'],
                                                             start_hours_on_wednesday = event_form.cleaned_data['start_hours_on_wednesday'],
                                                             end_hours_on_wednesday = event_form.cleaned_data['end_hours_on_wednesday'],
                                                             start_hours_on_thursday = event_form.cleaned_data['start_hours_on_thursday'],
                                                             end_hours_on_thursday = event_form.cleaned_data['end_hours_on_thursday'],
                                                             start_hours_on_friday = event_form.cleaned_data['start_hours_on_friday'],
                                                             end_hours_on_friday = event_form.cleaned_data['end_hours_on_friday'],
                                                             start_hours_on_saturday = event_form.cleaned_data['start_hours_on_saturday'],
                                                             end_hours_on_saturday = event_form.cleaned_data['end_hours_on_saturday'],
                                                             start_hours_on_sunday = event_form.cleaned_data['start_hours_on_sunday'],
                                                             end_hours_on_sunday = event_form.cleaned_data['end_hours_on_sunday'],
                                                             frequency = event_form.cleaned_data['frequency'],
                                                             interval = event_form.cleaned_data['interval'],
                                                             by_monthday = event_form.cleaned_data['ordinal_day'],
                                                             by_month = event_form.cleaned_data['ordinal'],
                                                             event_start_date = event_form.cleaned_data['date_started'],
                                                             event_completion_date = event_form.cleaned_data['date_completed'],
                                                             event_start_date1 = event_form.cleaned_data['date_started1'],
                                                             event_completion_date1 = event_form.cleaned_data['date_completed1'],
                                                             
                                                             event_start_date2 = event_form.cleaned_data['date_started2'],
                                                             event_completion_date2 = event_form.cleaned_data['date_completed2'],
                                                             
                                                             event_start_date3 = event_form.cleaned_data['date_started3'],
                                                             event_completion_date3 = event_form.cleaned_data['date_completed3'],
                                                             
                                                             event_start_date4 = event_form.cleaned_data['date_started4'],
                                                             event_completion_date4 = event_form.cleaned_data['date_completed4'],
                                                             event_start_date5 = event_form.cleaned_data['date_started5'],
                                                             event_completion_date5 = event_form.cleaned_data['date_completed5'],
                                                             frequency1 = event_form.cleaned_data['frequency1'],
                                                             interval1 = event_form.cleaned_data['interval1'],
                                                             by_monthday1 = event_form.cleaned_data['ordinal_day1'],
                                                             by_month1 = event_form.cleaned_data['ordinal1'],
                                                                                                                       
                                                             frequency2 = event_form.cleaned_data['frequency2'],
                                                             interval2 = event_form.cleaned_data['interval2'],
                                                             by_monthday2 = event_form.cleaned_data['ordinal_day2'],
                                                             by_month2 = event_form.cleaned_data['ordinal2'],
                                                             frequency3 = event_form.cleaned_data['frequency3'],
                                                             interval3 = event_form.cleaned_data['interval3'],
                                                             by_monthday3 = event_form.cleaned_data['ordinal_day3'],
                                                             by_month3 = event_form.cleaned_data['ordinal3'],
                                                             frequency4 = event_form.cleaned_data['frequency4'],
                                                             interval4 = event_form.cleaned_data['interval4'],
                                                             by_monthday4 = event_form.cleaned_data['ordinal_day4'],
                                                             by_month4 = event_form.cleaned_data['ordinal4'],
                                                             
                                                             
                                                             )

            #Copy last uploaded image to 'images' directory
            try:
                src= MEDIA_ROOT + '/images/tmp/'+ str(event_form.cleaned_data['event_poster'])
                dst= MEDIA_ROOT + '/images/'
                shutil.move(src,dst)
            except:
                pass


            #Variables used in all recurrences
            inter=int(event_form.cleaned_data['interval'])
            freq=event_form.cleaned_data['frequency']
            dicto={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
            
            inter1=int(event_form.cleaned_data['interval1'])
            freq1=event_form.cleaned_data['frequency1']
            dicto1={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
            
            inter2=int(event_form.cleaned_data['interval2'])
            freq2=event_form.cleaned_data['frequency2']
            dicto2={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
            
            inter3=int(event_form.cleaned_data['interval3'])
            freq3=event_form.cleaned_data['frequency3']
            dicto3={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
            
            inter4=int(event_form.cleaned_data['interval4'])
            freq4=event_form.cleaned_data['frequency4']
            dicto4={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
            
            
            #BUILD MULTIPLE SHOWTIMES FUNCTIONALITY
            
            #Performance Based events Performance records           
            if event_form.cleaned_data['schedule_type']=='performance_based':
                #Case of Frequency = Once
                if freq == "ONCE":
                    #Test of Showtime 1
                    if (event_form.cleaned_data['event_start_hours_1'] != None) and (event_form.cleaned_data['event_end_hours_1'] != None):
                        sh_start=event_form.cleaned_data['event_start_hours_1'] 
                        sh_end=event_form.cleaned_data['event_end_hours_1']
                        tix_price=event_form.cleaned_data['event_ticket_price_1']
                        performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                            ticket_price = tix_price,
                                                                                            date_of_performance = event_form.cleaned_data['date_started5'],                  
                                                                                            event = event_obj,
                                                                                            place = place_obj,
                                                                                            
                                                                                            showtimes_start = sh_start, 
                                                                                            showtimes_end = sh_end,                 
                                                                                            )
                   
                if freq1 == "ONCE":
                #Test of Showtime 1 under frequency 1
                    if (event_form.cleaned_data['event_start_hours_4'] != None) and (event_form.cleaned_data['event_end_hours_4'] != None):
                        sh_start=event_form.cleaned_data['event_start_hours_4'] 
                        sh_end=event_form.cleaned_data['event_end_hours_4']
                        tix_price=event_form.cleaned_data['event_ticket_price_4']
                        performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                            ticket_price = tix_price,
                                                                                            date_of_performance = event_form.cleaned_data['date_started1'],                  
                                                                                            event = event_obj,
                                                                                            place = place_obj,
                                                                                            
                                                                                            showtimes_start = sh_start, 
                                                                                            showtimes_end = sh_end,                 
                                                                                            )
                
                if freq2 == "ONCE":
                #Test of Showtime 1 under frequency 2
                    if (event_form.cleaned_data['event_start_hours_7'] != None) and (event_form.cleaned_data['event_end_hours_7'] != None):
                        sh_start=event_form.cleaned_data['event_start_hours_7'] 
                        sh_end=event_form.cleaned_data['event_end_hours_7']
                        tix_price=event_form.cleaned_data['event_ticket_price_7']
                        performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                            ticket_price = tix_price,
                                                                                            date_of_performance = event_form.cleaned_data['date_started2'],                  
                                                                                            event = event_obj,
                                                                                            place = place_obj,
                                                                                            
                                                                                            showtimes_start = sh_start, 
                                                                                            showtimes_end = sh_end,                 
                                                                                            )

                if freq3 == "ONCE":
                #Test of Showtime 1 under frequency 3
                    if (event_form.cleaned_data['event_start_hours_10'] != None) and (event_form.cleaned_data['event_end_hours_10'] != None):
                        sh_start=event_form.cleaned_data['event_start_hours_10'] 
                        sh_end=event_form.cleaned_data['event_end_hours_10']
                        tix_price=event_form.cleaned_data['event_ticket_price_10']
                        performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                            ticket_price = tix_price,
                                                                                            date_of_performance = event_form.cleaned_data['date_started3'],
                                                                                            event = event_obj,
                                                                                            place = place_obj,
                                                                                            
                                                                                            showtimes_start = sh_start, 
                                                                                            showtimes_end = sh_end,                 
                                                                                            )
                if freq4 == "ONCE":
                #Test of Showtime 1 under frequency 4
                    if (event_form.cleaned_data['event_start_hours_13'] != None) and (event_form.cleaned_data['event_end_hours_13'] != None):
                        sh_start=event_form.cleaned_data['event_start_hours_13'] 
                        sh_end=event_form.cleaned_data['event_end_hours_13']
                        tix_price=event_form.cleaned_data['event_ticket_price_13']
                        performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                            ticket_price = tix_price,
                                                                                            date_of_performance = event_form.cleaned_data['date_started4'],                  
                                                                                            event = event_obj,
                                                                                            place = place_obj,
                                                                                            
                                                                                            showtimes_start = sh_start, 
                                                                                            showtimes_end = sh_end,                 
                                                                                            )

                
                
                #Case of Frequency = Daily        
                if freq == "DAILY":
                    for ev in rrule.rrule(3, dtstart=event_form.cleaned_data['date_started5'], until=event_form.cleaned_data['date_completed5'], interval=inter):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_1'] != None) and (event_form.cleaned_data['event_end_hours_1'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_1'] 
                            sh_end=event_form.cleaned_data['event_end_hours_1']
                            tix_price=event_form.cleaned_data['event_ticket_price_1']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_2'] != None) and (event_form.cleaned_data['event_end_hours_2'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_2'] 
                            sh_end=event_form.cleaned_data['event_end_hours_2']
                            tix_price=event_form.cleaned_data['event_ticket_price_2']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_3'] != None) and (event_form.cleaned_data['event_end_hours_3'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_3'] 
                            sh_end=event_form.cleaned_data['event_end_hours_3']
                            tix_price=event_form.cleaned_data['event_ticket_price_3']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                
                
                #####################################
                #Case of Frequency2 = Daily        
                if freq1 == "DAILY":
                    for ev in rrule.rrule(3, dtstart=event_form.cleaned_data['date_started1'], until=event_form.cleaned_data['date_completed1'], interval=inter1):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_4'] != None) and (event_form.cleaned_data['event_end_hours_4'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_4'] 
                            sh_end=event_form.cleaned_data['event_end_hours_4']
                            tix_price=event_form.cleaned_data['event_ticket_price_4']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_5'] != None) and (event_form.cleaned_data['event_end_hours_6'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_5'] 
                            sh_end=event_form.cleaned_data['event_end_hours_5']
                            tix_price=event_form.cleaned_data['event_ticket_price_5']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_6'] != None) and (event_form.cleaned_data['event_end_hours_6'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_6'] 
                            sh_end=event_form.cleaned_data['event_end_hours_6']
                            tix_price=event_form.cleaned_data['event_ticket_price_6']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                
                #Case of Frequency2 = Daily        
                if freq2 == "DAILY":
                    for ev in rrule.rrule(3, dtstart=event_form.cleaned_data['date_started2'], until=event_form.cleaned_data['date_completed2'], interval=inter2):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_7'] != None) and (event_form.cleaned_data['event_end_hours_7'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_7'] 
                            sh_end=event_form.cleaned_data['event_end_hours_7']
                            tix_price=event_form.cleaned_data['event_ticket_price_7']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_8'] != None) and (event_form.cleaned_data['event_end_hours_8'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_8'] 
                            sh_end=event_form.cleaned_data['event_end_hours_8']
                            tix_price=event_form.cleaned_data['event_ticket_price_8']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_9'] != None) and (event_form.cleaned_data['event_end_hours_9'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_6'] 
                            sh_end=event_form.cleaned_data['event_end_hours_6']
                            tix_price=event_form.cleaned_data['event_ticket_price_6']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                
                #Case of Frequency3 = Daily
                
                if freq3 == "DAILY":
                    for ev in rrule.rrule(3, dtstart=event_form.cleaned_data['date_started3'], until=event_form.cleaned_data['date_completed3'], interval=inter3):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_10'] != None) and (event_form.cleaned_data['event_end_hours_10'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_10'] 
                            sh_end=event_form.cleaned_data['event_end_hours_10']
                            tix_price=event_form.cleaned_data['event_ticket_price_10']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_11'] != None) and (event_form.cleaned_data['event_end_hours_11'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_11'] 
                            sh_end=event_form.cleaned_data['event_end_hours_11']
                            tix_price=event_form.cleaned_data['event_ticket_price_11']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_12'] != None) and (event_form.cleaned_data['event_end_hours_12'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_12'] 
                            sh_end=event_form.cleaned_data['event_end_hours_12']
                            tix_price=event_form.cleaned_data['event_ticket_price_12']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                #Case of Frequency4 = Daily
                
                if freq4 == "DAILY":
                    for ev in rrule.rrule(3, dtstart=event_form.cleaned_data['date_started4'], until=event_form.cleaned_data['date_completed4'], interval=inter4):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_13'] != None) and (event_form.cleaned_data['event_end_hours_13'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_13'] 
                            sh_end=event_form.cleaned_data['event_end_hours_13']
                            tix_price=event_form.cleaned_data['event_ticket_price_13']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_14'] != None) and (event_form.cleaned_data['event_end_hours_14'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_14'] 
                            sh_end=event_form.cleaned_data['event_end_hours_14']
                            tix_price=event_form.cleaned_data['event_ticket_price_14']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_15'] != None) and (event_form.cleaned_data['event_end_hours_15'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_15'] 
                            sh_end=event_form.cleaned_data['event_end_hours_15']
                            tix_price=event_form.cleaned_data['event_ticket_price_15']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )

                
                #Case of Frequency = Weekly            
                if freq == "WEEKLY":
                    L=[i.week_day for i in event_form.cleaned_data['repeat_on']]
                    T=tuple([dicto[i] for i in L])
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started5'], until=event_form.cleaned_data['date_completed5'], interval=inter, byweekday=T):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_1'] != None) and (event_form.cleaned_data['event_end_hours_1'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_1'] 
                            sh_end=event_form.cleaned_data['event_end_hours_1']
                            tix_price=event_form.cleaned_data['event_ticket_price_1']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_2'] != None) and (event_form.cleaned_data['event_end_hours_2'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_2'] 
                            sh_end=event_form.cleaned_data['event_end_hours_2']
                            tix_price=event_form.cleaned_data['event_ticket_price_2']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_3'] != None) and (event_form.cleaned_data['event_end_hours_3'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_3'] 
                            sh_end=event_form.cleaned_data['event_end_hours_3']
                            tix_price=event_form.cleaned_data['event_ticket_price_3']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                            
                
                #Case of Frequency1 = Weekly            
                if freq1 == "WEEKLY":
                    L=[i.week_day for i in event_form.cleaned_data['repeat_on1']]
                    T=tuple([dicto[i] for i in L])
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started1'], until=event_form.cleaned_data['date_completed1'], interval=inter1, byweekday=T):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_4'] != None) and (event_form.cleaned_data['event_end_hours_4'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_4'] 
                            sh_end=event_form.cleaned_data['event_end_hours_4']
                            tix_price=event_form.cleaned_data['event_ticket_price_4']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_5'] != None) and (event_form.cleaned_data['event_end_hours_5'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_5'] 
                            sh_end=event_form.cleaned_data['event_end_hours_5']
                            tix_price=event_form.cleaned_data['event_ticket_price_5']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_6'] != None) and (event_form.cleaned_data['event_end_hours_6'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_6'] 
                            sh_end=event_form.cleaned_data['event_end_hours_6']
                            tix_price=event_form.cleaned_data['event_ticket_price_6']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                #Case of Frequency2 = Weekly
                if freq2 == "WEEKLY":
                    L=[i.week_day for i in event_form.cleaned_data['repeat_on1']]
                    T=tuple([dicto[i] for i in L])
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started2'], until=event_form.cleaned_data['date_completed2'], interval=inter2, byweekday=T):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_7'] != None) and (event_form.cleaned_data['event_end_hours_7'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_7'] 
                            sh_end=event_form.cleaned_data['event_end_hours_7']
                            tix_price=event_form.cleaned_data['event_ticket_price_7']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_8'] != None) and (event_form.cleaned_data['event_end_hours_8'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_8'] 
                            sh_end=event_form.cleaned_data['event_end_hours_8']
                            tix_price=event_form.cleaned_data['event_ticket_price_8']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_9'] != None) and (event_form.cleaned_data['event_end_hours_9'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_9'] 
                            sh_end=event_form.cleaned_data['event_end_hours_9']
                            tix_price=event_form.cleaned_data['event_ticket_price_9']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                #Case of Frequency3 = Weekly            
                if freq3 == "WEEKLY":
                    L=[i.week_day for i in event_form.cleaned_data['repeat_on3']]
                    T=tuple([dicto[i] for i in L])
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started3'], until=event_form.cleaned_data['date_completed3'], interval=inter3, byweekday=T):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_10'] != None) and (event_form.cleaned_data['event_end_hours_10'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_10'] 
                            sh_end=event_form.cleaned_data['event_end_hours_10']
                            tix_price=event_form.cleaned_data['event_ticket_price_10']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_11'] != None) and (event_form.cleaned_data['event_end_hours_11'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_11'] 
                            sh_end=event_form.cleaned_data['event_end_hours_11']
                            tix_price=event_form.cleaned_data['event_ticket_price_11']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_12'] != None) and (event_form.cleaned_data['event_end_hours_12'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_12'] 
                            sh_end=event_form.cleaned_data['event_end_hours_12']
                            tix_price=event_form.cleaned_data['event_ticket_price_12']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                #Case of Frequency4 = Weekly    
                if freq4 == "WEEKLY":
                    L=[i.week_day for i in event_form.cleaned_data['repeat_on4']]
                    T=tuple([dicto[i] for i in L])
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started4'], until=event_form.cleaned_data['date_completed4'], interval=inter4, byweekday=T):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_13'] != None) and (event_form.cleaned_data['event_end_hours_13'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_13'] 
                            sh_end=event_form.cleaned_data['event_end_hours_13']
                            tix_price=event_form.cleaned_data['event_ticket_price_13']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_14'] != None) and (event_form.cleaned_data['event_end_hours_14'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_14'] 
                            sh_end=event_form.cleaned_data['event_end_hours_14']
                            tix_price=event_form.cleaned_data['event_ticket_price_14']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_15'] != None) and (event_form.cleaned_data['event_end_hours_15'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_15'] 
                            sh_end=event_form.cleaned_data['event_end_hours_15']
                            tix_price=event_form.cleaned_data['event_ticket_price_15']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                
                #Case of Frequency = Monthly
                if freq == "MONTHLY":
                    mo_rpt_day=dicto[event_form.cleaned_data['ordinal_day']](int(event_form.cleaned_data['ordinal']),)
                    for ev in rrule.rrule(1, dtstart=event_form.cleaned_data['date_started5'], until=event_form.cleaned_data['date_completed5'], interval=inter, byweekday=mo_rpt_day):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_1'] != None) and (event_form.cleaned_data['event_end_hours_1'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_1'] 
                            sh_end=event_form.cleaned_data['event_end_hours_1']
                            tix_price=event_form.cleaned_data['event_ticket_price_1']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_2'] != None) and (event_form.cleaned_data['event_end_hours_2'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_2'] 
                            sh_end=event_form.cleaned_data['event_end_hours_2']
                            tix_price=event_form.cleaned_data['event_ticket_price_2']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_3'] != None) and (event_form.cleaned_data['event_end_hours_3'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_3'] 
                            sh_end=event_form.cleaned_data['event_end_hours_3']
                            tix_price=event_form.cleaned_data['event_ticket_price_3']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                
                #Case of Frequency1 = Monthly
                if freq1 == "MONTHLY":
                    mo_rpt_day=dicto[event_form.cleaned_data['ordinal_day1']](int(event_form.cleaned_data['ordinal1']),)
                    for ev in rrule.rrule(1, dtstart=event_form.cleaned_data['date_started1'], until=event_form.cleaned_data['date_completed1'], interval=inter1, byweekday=mo_rpt_day):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_4'] != None) and (event_form.cleaned_data['event_end_hours_4'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_4'] 
                            sh_end=event_form.cleaned_data['event_end_hours_4']
                            tix_price=event_form.cleaned_data['event_ticket_price_4']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_5'] != None) and (event_form.cleaned_data['event_end_hours_5'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_5'] 
                            sh_end=event_form.cleaned_data['event_end_hours_5']
                            tix_price=event_form.cleaned_data['event_ticket_price_5']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_6'] != None) and (event_form.cleaned_data['event_end_hours_6'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_6'] 
                            sh_end=event_form.cleaned_data['event_end_hours_6']
                            tix_price=event_form.cleaned_data['event_ticket_price_6']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                if freq2 == "MONTHLY":
                    mo_rpt_day=dicto[event_form.cleaned_data['ordinal_day2']](int(event_form.cleaned_data['ordinal2']),)
                    for ev in rrule.rrule(1, dtstart=event_form.cleaned_data['date_started2'], until=event_form.cleaned_data['date_completed2'], interval=inter2, byweekday=mo_rpt_day):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_7'] != None) and (event_form.cleaned_data['event_end_hours_7'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_7'] 
                            sh_end=event_form.cleaned_data['event_end_hours_7']
                            tix_price=event_form.cleaned_data['event_ticket_price_7']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_8'] != None) and (event_form.cleaned_data['event_end_hours_8'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_8'] 
                            sh_end=event_form.cleaned_data['event_end_hours_8']
                            tix_price=event_form.cleaned_data['event_ticket_price_8']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_9'] != None) and (event_form.cleaned_data['event_end_hours_9'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_9'] 
                            sh_end=event_form.cleaned_data['event_end_hours_9']
                            tix_price=event_form.cleaned_data['event_ticket_price_9']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                if freq3 == "MONTHLY":
                    mo_rpt_day=dicto[event_form.cleaned_data['ordinal_day3']](int(event_form.cleaned_data['ordinal3']),)
                    for ev in rrule.rrule(1, dtstart=event_form.cleaned_data['date_started3'], until=event_form.cleaned_data['date_completed3'], interval=inter3, byweekday=mo_rpt_day):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_10'] != None) and (event_form.cleaned_data['event_end_hours_10'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_10'] 
                            sh_end=event_form.cleaned_data['event_end_hours_10']
                            tix_price=event_form.cleaned_data['event_ticket_price_10']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_11'] != None) and (event_form.cleaned_data['event_end_hours_11'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_11'] 
                            sh_end=event_form.cleaned_data['event_end_hours_11']
                            tix_price=event_form.cleaned_data['event_ticket_price_11']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_12'] != None) and (event_form.cleaned_data['event_end_hours_12'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_12'] 
                            sh_end=event_form.cleaned_data['event_end_hours_12']
                            tix_price=event_form.cleaned_data['event_ticket_price_12']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                if freq4 == "MONTHLY":
                    mo_rpt_day=dicto[event_form.cleaned_data['ordinal_day4']](int(event_form.cleaned_data['ordinal4']),)
                    for ev in rrule.rrule(1, dtstart=event_form.cleaned_data['date_started4'], until=event_form.cleaned_data['date_completed4'], interval=inter4, byweekday=mo_rpt_day):
                        date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                        #Test of Showtime 1
                        if (event_form.cleaned_data['event_start_hours_13'] != None) and (event_form.cleaned_data['event_end_hours_13'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_13'] 
                            sh_end=event_form.cleaned_data['event_end_hours_13']
                            tix_price=event_form.cleaned_data['event_ticket_price_13']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 2
                        if (event_form.cleaned_data['event_start_hours_14'] != None) and (event_form.cleaned_data['event_end_hours_14'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_14'] 
                            sh_end=event_form.cleaned_data['event_end_hours_14']
                            tix_price=event_form.cleaned_data['event_ticket_price_14']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )
                        #Test of Showtime 3
                        if (event_form.cleaned_data['event_start_hours_15'] != None) and (event_form.cleaned_data['event_end_hours_15'] != None):
                            sh_start=event_form.cleaned_data['event_start_hours_15'] 
                            sh_end=event_form.cleaned_data['event_end_hours_15']
                            tix_price=event_form.cleaned_data['event_ticket_price_15']
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = tix_price,
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = sh_start, 
                                                                                                showtimes_end = sh_end,
                                                                                                )            
            
            #Open Hour Based Performance Records
            if event_form.cleaned_data['schedule_type']=='open_hour_based':
                if (event_form.cleaned_data['start_hours_on_monday'] != None) and (event_form.cleaned_data['end_hours_on_monday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.MO):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_monday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_monday'],
                                                                                                )
                if (event_form.cleaned_data['start_hours_on_tuesday'] != None) and (event_form.cleaned_data['end_hours_on_tuesday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.TU):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_tuesday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_tuesday'],
                                                                                                )
                if (event_form.cleaned_data['start_hours_on_wednesday'] != None) and (event_form.cleaned_data['end_hours_on_wednesday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.WE):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_wednesday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_wednesday'],
                                                                                                )
                if (event_form.cleaned_data['start_hours_on_thursday'] != None) and (event_form.cleaned_data['end_hours_on_thursday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.TH):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                 
                                                                                                event = event_obj,
                                                                                                place = place_obj,                                                                                                
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_thursday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_thursday'],
                                                                                                )
                if (event_form.cleaned_data['start_hours_on_friday'] != None) and (event_form.cleaned_data['end_hours_on_friday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.FR):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,                                                                                                
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_friday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_friday'],
                                                                                                )
                if (event_form.cleaned_data['start_hours_on_saturday'] != None) and (event_form.cleaned_data['end_hours_on_saturday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.SA):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,                                                                                                
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_saturday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_saturday'],
                                                                                                )
                if (event_form.cleaned_data['start_hours_on_sunday'] != None) and (event_form.cleaned_data['end_hours_on_sunday'] != None):
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=rrule.SU):
                            date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
                            performance_obj, created = PerformanceDetails.objects.get_or_create(
                                                                                                ticket_price = event_form.cleaned_data['event_ticket_price'],
                                                                                                date_of_performance = date_show,                  
                                                                                                event = event_obj,
                                                                                                place = place_obj,                                                                                                
                                                                                                showtimes_start = event_form.cleaned_data['start_hours_on_sunday'], 
                                                                                                showtimes_end = event_form.cleaned_data['end_hours_on_sunday'],
                                                                                                )

            
            for days in event_form.cleaned_data['repeat_on']:
                event_obj.by_day.add(days.id)
            for genre in event_form.cleaned_data['event_genre']:
                event_obj.event_genre.add(genre.id)
            for public in event_form.cleaned_data['event_public']:
                event_obj.event_public.add(public.id)
                
            for days1 in event_form.cleaned_data['repeat_on1']:
                event_obj.by_day1.add(days1.id)

            for days2 in event_form.cleaned_data['repeat_on2']:
                event_obj.by_day2.add(days2.id)
            for days3 in event_form.cleaned_data['repeat_on3']:
                event_obj.by_day3.add(days3.id)
            for days4 in event_form.cleaned_data['repeat_on4']:
                event_obj.by_day4.add(days4.id)
            try:
                old_event_obj.delete()
            except:
                pass
            return HttpResponseRedirect('/myprofile/home/')
            
        else:
            print "Form is not valid"
            event_poster=''
            
    else:
        event_form = EventForm()
        eventposter_form = EventPosterForm()
        event_poster = ""
        try:
            id = request.GET['id']
            event_obj = Event.objects.get(id=id)
            performance_obj = Event.objects.get(id=id).performancedetails_set.values("showtimes_start","showtimes_end","ticket_price").annotate(Count('showtimes_start'), Count('showtimes_end'), Count('ticket_price'))
            event_form.fields['title'].initial = event_obj.title
            event_form.fields['eventwebsite'].initial = event_obj.eventwebsite
            event_form.fields['description'].initial = event_obj.description
            event_form.fields['venue_name'].initial = event_obj.location
            event_form.fields['category'].initial = event_obj.category
            event_form.fields['schedule_type'].initial = event_obj.schedule_type
            event_form.fields['street_address'].initial = event_obj.location
            event_form.fields['date_started'].initial = event_obj.event_start_date
            event_form.fields['date_completed'].initial = event_obj.event_completion_date
            
            event_form.fields['date_started1'].initial = event_obj.event_start_date1
            event_form.fields['date_completed1'].initial = event_obj.event_completion_date1
            event_form.fields['date_started2'].initial = event_obj.event_start_date2
            event_form.fields['date_completed2'].initial = event_obj.event_completion_date2
            event_form.fields['date_started3'].initial = event_obj.event_start_date3
            event_form.fields['date_completed3'].initial = event_obj.event_completion_date3
            event_form.fields['date_started4'].initial = event_obj.event_start_date4
            event_form.fields['date_completed4'].initial = event_obj.event_completion_date4
            event_form.fields['date_started5'].initial = event_obj.event_start_date5
            event_form.fields['date_completed5'].initial = event_obj.event_completion_date5
            # For Performance Based
            if event_form.fields['schedule_type'].initial == "performance_based":
                # ----1
                try:
                    if performance_obj[0].get('showtimes_start'):
                        event_form.fields['event_start_hours_1'].initial = performance_obj[0].get('showtimes_start')
                        event_form.fields['event_end_hours_1'].initial = performance_obj[0].get('showtimes_end')
                        event_form.fields['event_ticket_price_1'].initial = performance_obj[0].get('ticket_price')
                except:
                    pass
                # ----2
                try:
                    if performance_obj[1].get('showtimes_start'):
                        event_form.fields['event_start_hours_2'].initial = performance_obj[1].get('showtimes_start')
                        event_form.fields['event_end_hours_2'].initial = performance_obj[1].get('showtimes_end')
                        event_form.fields['event_ticket_price_2'].initial = performance_obj[1].get('ticket_price')
                except:
                    pass
                
                # ----3
                try:
                    print performance_obj[2]
                    if performance_obj[2].get('showtimes_start'):
                        event_form.fields['event_start_hours_3'].initial = performance_obj[2].get('showtimes_start')
                        event_form.fields['event_end_hours_3'].initial = performance_obj[2].get('showtimes_end')
                        event_form.fields['event_ticket_price_3'].initial = performance_obj[2].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[3].get('showtimes_start'):
                        event_form.fields['event_start_hours_4'].initial = performance_obj[3].get('showtimes_start')
                        event_form.fields['event_end_hours_4'].initial = performance_obj[3].get('showtimes_end')
                        event_form.fields['event_ticket_price_4'].initial = performance_obj[3].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[4].get('showtimes_start'):
                        event_form.fields['event_start_hours_5'].initial = performance_obj[4].get('showtimes_start')
                        event_form.fields['event_end_hours_5'].initial = performance_obj[4].get('showtimes_end')
                        event_form.fields['event_ticket_price_5'].initial = performance_obj[4].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[5].get('showtimes_start'):
                        event_form.fields['event_start_hours_6'].initial = performance_obj[5].get('showtimes_start')
                        event_form.fields['event_end_hours_6'].initial = performance_obj[5].get('showtimes_end')
                        event_form.fields['event_ticket_price_6'].initial = performance_obj[5].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[6].get('showtimes_start'):
                        event_form.fields['event_start_hours_7'].initial = performance_obj[6].get('showtimes_start')
                        event_form.fields['event_end_hours_7'].initial = performance_obj[6].get('showtimes_end')
                        event_form.fields['event_ticket_price_7'].initial = performance_obj[6].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[7].get('showtimes_start'):
                        event_form.fields['event_start_hours_8'].initial = performance_obj[7].get('showtimes_start')
                        event_form.fields['event_end_hours_8'].initial = performance_obj[7].get('showtimes_end')
                        event_form.fields['event_ticket_price_8'].initial = performance_obj[7].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[8].get('showtimes_start'):
                        event_form.fields['event_start_hours_9'].initial = performance_obj[8].get('showtimes_start')
                        event_form.fields['event_end_hours_9'].initial = performance_obj[8].get('showtimes_end')
                        event_form.fields['event_ticket_price_9'].initial = performance_obj[8].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[9].get('showtimes_start'):
                        event_form.fields['event_start_hours_10'].initial = performance_obj[9].get('showtimes_start')
                        event_form.fields['event_end_hours_10'].initial = performance_obj[9].get('showtimes_end')
                        event_form.fields['event_ticket_price_10'].initial = performance_obj[9].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[10].get('showtimes_start'):
                        event_form.fields['event_start_hours_11'].initial = performance_obj[10].get('showtimes_start')
                        event_form.fields['event_end_hours_11'].initial = performance_obj[10].get('showtimes_end')
                        event_form.fields['event_ticket_price_11'].initial = performance_obj[10].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[11].get('showtimes_start'):
                        event_form.fields['event_start_hours_12'].initial = performance_obj[11].get('showtimes_start')
                        event_form.fields['event_end_hours_12'].initial = performance_obj[11].get('showtimes_end')
                        event_form.fields['event_ticket_price_12'].initial = performance_obj[11].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[12].get('showtimes_start'):
                        event_form.fields['event_start_hours_13'].initial = performance_obj[12].get('showtimes_start')
                        event_form.fields['event_end_hours_13'].initial = performance_obj[12].get('showtimes_end')
                        event_form.fields['event_ticket_price_13'].initial = performance_obj[12].get('ticket_price')
                except:
                    pass
                
                try:
                    if performance_obj[13].get('showtimes_start'):
                        event_form.fields['event_start_hours_14'].initial = performance_obj[13].get('showtimes_start')
                        event_form.fields['event_end_hours_14'].initial = performance_obj[13].get('showtimes_end')
                        event_form.fields['event_ticket_price_14'].initial = performance_obj[13].get('ticket_price')
                except:
                    pass
                try:
                    if performance_obj[14].get('showtimes_start'):
                        event_form.fields['event_start_hours_15'].initial = performance_obj[14].get('showtimes_start')
                        event_form.fields['event_end_hours_15'].initial = performance_obj[14].get('showtimes_end')
                        event_form.fields['event_ticket_price_15'].initial = performance_obj[14].get('ticket_price')
                except:
                    pass
                
                event_form.fields['frequency'].initial = event_obj.frequency
                event_form.fields['interval'].initial = event_obj.interval
                event_form.fields['repeat_on'].initial = [days for days in event_obj.by_day.all()]
                event_form.fields['ordinal_day'].initial = event_obj.by_monthday
                event_form.fields['ordinal'].initial = event_obj.by_month
                
                event_form.fields['frequency1'].initial = event_obj.frequency1
                event_form.fields['interval1'].initial = event_obj.interval1
                event_form.fields['repeat_on1'].initial = [days1 for days1 in event_obj.by_day1.all()]
                event_form.fields['ordinal_day1'].initial = event_obj.by_monthday1
                event_form.fields['ordinal1'].initial = event_obj.by_month1
                
                event_form.fields['frequency2'].initial = event_obj.frequency2
                event_form.fields['interval2'].initial = event_obj.interval2
                event_form.fields['repeat_on2'].initial = [days2 for days2 in event_obj.by_day2.all()]
                event_form.fields['ordinal_day2'].initial = event_obj.by_monthday2
                event_form.fields['ordinal2'].initial = event_obj.by_month2
                
                event_form.fields['frequency3'].initial = event_obj.frequency3
                event_form.fields['interval3'].initial = event_obj.interval3
                event_form.fields['repeat_on3'].initial = [days3 for days3 in event_obj.by_day3.all()]
                event_form.fields['ordinal_day3'].initial = event_obj.by_monthday3
                event_form.fields['ordinal3'].initial = event_obj.by_month3
                
                event_form.fields['frequency4'].initial = event_obj.frequency4
                event_form.fields['interval4'].initial = event_obj.interval4
                event_form.fields['repeat_on4'].initial = [days4 for days4 in event_obj.by_day4.all()]
                event_form.fields['ordinal_day4'].initial = event_obj.by_monthday4
                event_form.fields['ordinal4'].initial = event_obj.by_month4
                
            # For OpenHour Based
            elif event_form.fields['schedule_type'].initial == "open_hour_based":
                event_form.fields['start_hours_on_monday'].initial = event_obj.start_hours_on_monday
                event_form.fields['end_hours_on_monday'].initial = event_obj.end_hours_on_monday
                event_form.fields['start_hours_on_tuesday'].initial = event_obj.start_hours_on_tuesday
                event_form.fields['end_hours_on_tuesday'].initial = event_obj.end_hours_on_tuesday
                event_form.fields['start_hours_on_wednesday'].initial = event_obj.start_hours_on_wednesday
                event_form.fields['end_hours_on_wednesday'].initial = event_obj.end_hours_on_wednesday
                event_form.fields['start_hours_on_thursday'].initial = event_obj.start_hours_on_thursday
                event_form.fields['end_hours_on_thursday'].initial = event_obj.end_hours_on_thursday
                event_form.fields['start_hours_on_friday'].initial = event_obj.start_hours_on_friday
                event_form.fields['end_hours_on_friday'].initial = event_obj.end_hours_on_friday
                event_form.fields['start_hours_on_saturday'].initial = event_obj.start_hours_on_saturday
                event_form.fields['end_hours_on_saturday'].initial = event_obj.end_hours_on_saturday
                event_form.fields['start_hours_on_sunday'].initial = event_obj.start_hours_on_sunday
                event_form.fields['end_hours_on_sunday'].initial = event_obj.end_hours_on_sunday
                event_form.fields['event_ticket_price'].initial = event_obj.performancedetails_set.values('ticket_price')[0].get('ticket_price')
            
            
            event_form.fields['event_genre'].initial = [event_genre.id for event_genre in event_obj.event_genre.all()]
            event_form.fields['event_public'].initial = [event_public.id for event_public in event_obj.event_public.all()]
            
            try:
                event_poster = event_obj.event_poster
            except:
                event_poster = ""
            
        except:
            pass 
            
    frequency_range = {"daily":range(6),"weekly":range(4),"monthly":range(12)}
    return render_to_response('event/event.html',
                              {
                               'eventform':event_form,
                               'eventform_poster':eventposter_form,
                               'frequency_range':frequency_range,
                               'event_poster': event_poster,
                               'active_link': "publish"
                               },
                              context_instance=RequestContext(request)
                              )
    
#----------------------------------------------------------------------------#
def splash(request):
    events = Event.objects.all().order_by("id")[0:50]
    return render_to_response("splash2.html",
                              {"events":events},
                              context_instance=RequestContext(request)
                              )
    
#----------------------------------------------------------------------------#
def home(request):
    category = Category.objects.all()
    return render_to_response("event/home_page.html",
                              {
                               "request":request,
                               "category":category,
                               "active_link":"home"
                               },
                              context_instance=RequestContext(request)
                              )
    
#----------------------------------------------------------------------------#
def handle_uploaded_file(request):
    event_poster = request.FILES['event_poster_file']
    
    import PIL
    from PIL import Image
    from cStringIO import StringIO
    from django.core.files.uploadedfile import InMemoryUploadedFile
    
    poster_wip = Image.open(event_poster)
    owidth= poster_wip.size[0]
    oheight = poster_wip.size[1]
    if owidth > oheight:
        if oheight <= 200:
            pass
        else:
            maxSize=(200*owidth/oheight, 200)
            poster_wip.thumbnail(maxSize, Image.ANTIALIAS)
        
    else:
        if owidth <= 150:
            pass
        else:
            maxSize=(150, 150*oheight/owidth)
            poster_wip.thumbnail(maxSize, Image.ANTIALIAS)
    
    resized_posterFile = StringIO()
    poster_wip.save(resized_posterFile, "JPEG")
    resized_posterFile.seek(0)
    
    posterFile=InMemoryUploadedFile(resized_posterFile, None, str(event_poster), 'image/jpeg', len(resized_posterFile.getvalue()), None)
    destination = open(MEDIA_ROOT + '/images/tmp/'+ str(event_poster), 'wb+')
    for chunk in posterFile.chunks():
        destination.write(chunk)
    
    destination.close()

    return HttpResponse(str(event_poster))

#----------------------------------------------------------------------------#
def event_list(request):
    import datetime
    from datetime import datetime
    
    kwargs = {
              'status':True,
             }
    
    kwargs1 = {}
    kwargs2 = {}
    searchbox_q = Q()
    category_q = Q()
    audience_q = Q()
    start_time_q = Q()
    end_time_q = Q()
    event_date = ""
    event_date_end = ""
    event_date_end_object = ""
    try:
        if request.GET['event_date']:
            event_date = request.GET['event_date'];
            event_date_object = datetime.strptime(event_date, "%Y-%m-%d")
    except:
        pass
    
    try:
        if request.GET['event_date_end']:
            event_date_end = request.GET['event_date_end'];
            event_date_end_object = datetime.strptime(event_date_end, "%Y-%m-%d")
    except:
        pass
    
    if event_date!="" and event_date_end!="":
        kwargs1['event_start_date__gte'] = request.GET['event_date']
        kwargs1['event_start_date__lte'] = request.GET['event_date_end']
        kwargs2['event_completion_date__gte'] = request.GET['event_date']
        kwargs2['event_completion_date__lte'] = request.GET['event_date_end']
    elif event_date!="":
        kwargs1['event_start_date__lte'] = request.GET['event_date']
        kwargs1['event_completion_date__gte'] = request.GET['event_date']
         
    try:
        if request.GET['min_price']:
            kwargs['performancedetails__ticket_price__gte'] = request.GET['min_price']
    except:
        pass
    
    try:
        if request.GET['max_price']:
            kwargs['performancedetails__ticket_price__lte'] = request.GET['max_price']
    except:
        pass
    
    try:
        if request.GET['search_text']:
            word_list=request.GET['search_text'].split()
            list_title_qs=[Q(title__icontains=x) for x in word_list]
            list_description_qs=[Q(description__icontains=x) for x in word_list]
#            list_location_qs=[Q(location__icontains=x) for x in word_list] // FOREIGN FIELD NEEDS Place__location etc.
            
            searchbox_q=reduce(or_, list_title_qs + list_description_qs)
#            kwargs['title__icontains'] = request.GET['search_text']
    except:
        pass
    
    try:

        if request.GET['start_time']:
            spl = [Q(schedule_type='performance_based'), Q(performancedetails__showtimes_start__gte=request.GET['start_time'])]
            spl_qs = reduce(and_, spl)
            sol = [Q(schedule_type='open_hour_based'), Q(performancedetails__showtimes_start__lte=request.GET['start_time']), Q(performancedetails__showtimes_end__gte=request.GET['start_time'])]
            sol_qs = reduce(and_, sol)
            start_time_q = reduce(or_, (spl_qs , sol_qs))
#            kwargs['performancedetails__showtimes_start__gte'] = request.GET['start_time']
    except:
        pass

    try:
        if request.GET['end_time']:
            epl = [Q(schedule_type='performance_based'), Q(performancedetails__showtimes_end__lte=request.GET['end_time'])]
            epl_qs = reduce(and_, epl)
            eol = [Q(schedule_type='open_hour_based'), Q(performancedetails__showtimes_start__lt=request.GET['end_time'])]
            eol_qs = reduce(and_, eol)
            end_time_q = reduce(or_, (epl_qs , eol_qs))

    except:
        pass

    
    try:
        if request.GET['category']:
            l_cat = request.GET.getlist('category')
            list_category_qs=[Q(category__exact=x) for x in l_cat]
            category_q=reduce(or_, list_category_qs)
    except:
        pass
    
    try:
        if request.GET['audience']:          
            l_aud = request.GET.getlist('audience')
            list_audience_qs=[Q(event_public__exact=x) for x in l_aud]
            audience_q=reduce(or_, list_audience_qs)
    except:
        pass
    
    try:
        if request.GET['page']:
            page = int(request.GET['page']) - 1
    except:
        
        page = 0
    
    limit = 30
    start = page*limit
    end = (page+1)*limit
    
    try:
        #If there is a mistake with the hours submitted by user
        if request.GET['ctrl']:
            return render_to_response("event/event_list.html")
#        else:
#            events = Event.objects.filter((Q(**kwargs1)|Q(**kwargs2))&start_time_q&end_time_q&searchbox_q&Q(**kwargs)&category_q&audience_q).distinct()
#            print events.query
#            return render_to_response("event/event_list.html",
#                               {
#                               "request":request,
#                               "events":events,
#                               },
#                              context_instance=RequestContext(request)
#                              )    
    except:
        events = Event.objects.filter((Q(**kwargs1)|Q(**kwargs2))&start_time_q&end_time_q&searchbox_q&Q(**kwargs)&category_q&audience_q).distinct()[start:end]
        event_obj1 = [event.performancedetails_set.aggregate(Max('ticket_price')) for event in events]
        #If view requested is 'by category'
    
    if (request.GET['tgl']!="0"):
        if(request.GET['sort']):
            if request.GET['sort'] == "showtimes_start":
                sort = "performancedetails__showtimes_start"
            elif request.GET['sort'] == "showtimes_end":
                sort = "-performancedetails__showtimes_start"
            elif request.GET['sort'] == "date_up":
                sort = "event_start_date"
            elif request.GET['sort'] == "date_down":
                sort = "-event_start_date"
            else:
                sort = "id"
            
            events_mov=events.filter(category=1).order_by(sort)
            #print sorted([event.performancedetails_set.aggregate(Max('ticket_price')) for event in events_mov])
            events_exh=events.filter(category=2).order_by(sort)
            events_lec=events.filter(category=3).order_by(sort)
            events_con=events.filter(category=4).order_by(sort)
            events_spo=events.filter(category=5).order_by(sort)
            events_the=events.filter(category=6).order_by(sort)
            events_ope=events.filter(category=7).order_by(sort)
            events_dan=events.filter(category=8).order_by(sort)
            events_mus=events.filter(category=9).order_by(sort)
            events_out=events.filter(category=10).order_by(sort)
            events_fes=events.filter(category=11).order_by(sort)
            events_sta=events.filter(category=12).order_by(sort)
            events_cou=events.filter(category=13).order_by(sort)
            events_cit=events.filter(category=14).order_by(sort)
            events_fai=events.filter(category=15).order_by(sort)
            events_fun=events.filter(category=16).order_by(sort)
            events_par=events.filter(category=17).order_by(sort)
        else:
            events_mov=events.filter(category=1)
            events_exh=events.filter(category=2)
            events_lec=events.filter(category=3)
            events_con=events.filter(category=4)
            events_spo=events.filter(category=5)
            events_the=events.filter(category=6)
            events_ope=events.filter(category=7)
            events_dan=events.filter(category=8)
            events_mus=events.filter(category=9)
            events_out=events.filter(category=10)
            events_fes=events.filter(category=11)
            events_sta=events.filter(category=12)
            events_cou=events.filter(category=13)
            events_cit=events.filter(category=14)
            events_fai=events.filter(category=15)
            events_fun=events.filter(category=16)
            events_par=events.filter(category=17)

        return render_to_response("event/event_list_cat.html",
                           {
                           "request":request,
                           "events_mov":events_mov,
                           "events_exh":events_exh,
                           "events_lec":events_lec,
                           "events_con":events_con,
                           "events_spo":events_spo,
                           "events_the":events_the,
                           "events_ope":events_ope,
                           "events_dan":events_dan,
                           "events_mus":events_mus,
                           "events_out":events_out,
                           "events_fes":events_fes,
                           "events_sta":events_sta,
                           "events_cou":events_cou,
                           "events_cit":events_cit,
                           "events_fai":events_fai,
                           "events_fun":events_fun,
                           "events_par":events_par,
                           "date_start":event_date_object,
                           "date_end":event_date_end_object,
                           },
                          context_instance=RequestContext(request)
                          ) 
    else:
        show_like = {}
        for event in events.iterator():
            show_like[event.id] = 1
            for popularity in event.popularity_set.iterator():
                if popularity.user_id == request.user.id:
                    show_like[event.id] = 0
        
        return render_to_response("event/event_list.html",
                           {
                           "request":request,
                           "events":events,
                           "date_end":event_date_end_object,
                           "date_start":event_date_object,
                           "page":page,
                           "show_like":show_like
                           },
                          context_instance=RequestContext(request)
                          )
     
#----------------------------------------------------------------------------#
def get_event_genre(request):  
    type = request.GET['type']
    category_obj = Category.objects.get(id=type)
    return render_to_response("event/event_genre.html",
                             {"genre_list":category_obj.eventgenre_set.all()},
                             context_instance=RequestContext(request)
                             )
    
def calendar(request):
    now = datetime.datetime.now()
    
    try:
        current_date = datetime.datetime(int(request.GET["year"]),int(request.GET["month"]),1)
        preset = "yes"
    except:
        current_date = datetime.datetime(int(now.year),int(now.month),1)
        preset = "no"
        
    prev_month=current_date+relativedelta(months=-1)
    prev_year=current_date+relativedelta(years=-1)
    next_month=current_date+relativedelta(months=+1)
    next_year=current_date+relativedelta(years=+1)
    daysrange = monthrange(current_date.year,current_date.month)
    weekday = current_date.isoweekday()
    
    if current_date.year == now.year and current_date.month == now.month:
        check_current_month = 1
    else:
        check_current_month = 0
    
    return render_to_response("event/calendar.html",
                             {
                                "prev_month":prev_month,
                                "prev_year":prev_year,
                                "next_month":next_month,
                                "next_year":next_year,
                                "current_date":current_date,
                                "daysrange":range(daysrange[1]),
                                "check_current_month":check_current_month,
                                "weekday":range(weekday%7),
                                "last_weekday":(weekday%7)+1,
                                "now":now,
                                "preset":preset
                            },
                             context_instance=RequestContext(request)
                             )

#----------------------------------------------------------------------------#
def get_event_details(request):
    id = request.GET['id']
    event_obj = Event.objects.get(id=id)
    by_day = {}
    oh_ticket_price = 0

    if event_obj.schedule_type == "open_hour_based":
        if event_obj.start_hours_on_monday and event_obj.end_hours_on_monday:
            by_day["Mon"] = {"start":event_obj.start_hours_on_monday,"end":event_obj.end_hours_on_monday}
            oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
        if event_obj.start_hours_on_tuesday and event_obj.end_hours_on_tuesday:
            by_day["Tues"] = {"start":event_obj.start_hours_on_tuesday,"end":event_obj.end_hours_on_tuesday}
            oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
        if event_obj.start_hours_on_wednesday and event_obj.end_hours_on_wednesday:
           by_day["Wed"] = {"start":event_obj.start_hours_on_wednesday,"end":event_obj.end_hours_on_wednesday}
           oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
        if event_obj.start_hours_on_thursday and event_obj.end_hours_on_thursday:
           by_day["Thu"] = {"start":event_obj.start_hours_on_thursday,"end":event_obj.end_hours_on_thursday}
           oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
        if event_obj.start_hours_on_friday and event_obj.end_hours_on_friday:
            by_day["Fri"] = {"start":event_obj.start_hours_on_friday,"end":event_obj.end_hours_on_friday}
            oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
        if event_obj.start_hours_on_saturday and event_obj.end_hours_on_saturday:
            by_day["Sat"] = {"start":event_obj.start_hours_on_saturday,"end":event_obj.end_hours_on_saturday}
            oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
        if event_obj.start_hours_on_sunday and event_obj.end_hours_on_sunday:
            by_day["Sun"] = {"start":event_obj.start_hours_on_sunday,"end":event_obj.end_hours_on_sunday}
            oh_ticket_price = event_obj.performancedetails_set.all()[0].ticket_price
                  
       
    if request.user.is_authenticated():
        user = request.user
        history_obj = History.objects.create(
                            event = event_obj,
                            user = user
                        )
        
    
    if request.method == "POST":
        ratings_form = EventRatingForm(request.POST)
        if ratings_form.is_valid():
            
            data = {
                'title':ratings_form.cleaned_data['title'],
                'ratings':ratings_form.cleaned_data['ratings'],
                'reviews':ratings_form.cleaned_data['reviews'],
                'event_id':id,
                'user':request.user
            }
            
            try:
                if request.POST['id']:
                    data['id'] = request.POST['id']
            except:
                pass
                
            comment_obj = UserComments(
                **data
            )
            comment_obj.save();
            #request.session['message'] = "Your Comment has been sent for approval"
            return HttpResponseRedirect('/event/details/?id='+id)
    else:
        ratings_form = EventRatingForm()
    
    try:
        sort_type = request.GET['sort_type']
    except:
        sort_type = ""
    if sort_type=="asc":
        user_comments = UserComments.objects.filter(event_id=id).filter(status=True).order_by("id")
    else:
        user_comments = UserComments.objects.filter(event_id=id).filter(status=True).order_by("-id")
    
    total_stars = range(1,6)
    total_stars_average = range(1,6)
    comment_counter = 0
    comment_total = 0
    for comment in user_comments:
        comment_counter+=1
        comment_total+=comment.ratings
    
    try:
        average_ratings = comment_total/comment_counter
    except:
        average_ratings = 3
    
    event_performance_values = PerformanceDetails.objects.filter(event_id=id).values("showtimes_start","showtimes_end","ticket_price").annotate(Count('showtimes_start'), Count('showtimes_end'), Count('ticket_price'))
    
    days1 = []
    days2 = []
    for days in event_obj.by_day.all():
        days1.append(days)
        
    for days in Days.objects.all():
        days2.append(days)
        
    total_days_consecutive = 0
    first_day = ""
    last_day = ""
    try:
        first_day = days1[0]
    except:
        first_day = ""
        last_day = ""
    
    if first_day:
        active = 0
        
        for x,y in enumerate(days2):
            try:
                current_day = days1[x]
            except:
                current_day = None
                
            if y == current_day:
                active = 1
            
            if active == 1:
                try:
                    if y != current_day:
                        last_day = days1[x-1]
                    else:
                        total_days_consecutive += 1
                except:
                    pass
    
    show_like = 1
    for popularity in event_obj.popularity_set.iterator():
        if popularity.user_id == request.user.id:
            show_like = 0
    
    return render_to_response("event/event_detail.html",
                              {
                               "eventdetails":event_obj,
                              "event_performance":event_obj.performancedetails_set.all(),
                              "oh_ticket_price":oh_ticket_price,
                              "ratings_form":ratings_form,
                              "user_comments":user_comments,
                              "total_stars":total_stars,
                              "average_ratings":average_ratings,
                              "sort_type":sort_type,
                              "total_days_consecutive":total_days_consecutive,
                              "first_day":str(first_day)[:3],
                              "last_day":str(last_day)[:3],
                              "event_performance_values": event_performance_values,
                              'by_day':by_day,
                              "comment_counter":comment_counter,
                              "host":settings.HOST,
                              "page_url":request.get_full_path,
                              "show_like":show_like
                              },
                              context_instance=RequestContext(request)
                              )
#----------------------------------------------------------------------------#
def update_city(request):
    city = request.GET['city']
    request.session['city'] = city
    return HttpResponse(str(city))
#----------------------------------------------------------------------------#

def comment_delete(request):
    comment_id = request.GET['id']
    comment_obj = UserComments.objects.get(id=comment_id)
    comment_obj.delete()
    
    event_id = request.GET['event_id']
    return HttpResponseRedirect('/event/details/?id='+event_id)
#----------------------------------------------------------------------------#    