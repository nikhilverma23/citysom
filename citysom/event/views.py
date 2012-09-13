# Create your views here.
import sys
from citysom.event.models import Place, Event, Category, PerformanceDetails, UserComments, Days
from django.shortcuts import render_to_response
from django.template import RequestContext
from citysom.event.forms import EventForm, EventPosterForm, EventRatingForm
from django.http import Http404, HttpResponse,HttpResponseRedirect, HttpResponseServerError
from django.template import loader, Context
import datetime
import dateutil
from dateutil import rrule
import shutil
from django import http
from django.contrib.auth.decorators import login_required
from citysom.settings import MEDIA_ROOT,STATIC_ROOT
from operator import or_, and_
from django.db.models import Q, Count
from citysom.myprofile.models import History

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
                                                                                            #date_started = event_form.cleaned_data['date_started'],
                                                                                            #date_completed = event_form.cleaned_data['date_completed'],                  
                                                                                            event = event_obj,
                                                                                            place = place_obj,
                                                                                            
                                                                                            showtimes_start = sh_start, 
                                                                                            showtimes_end = sh_end,                 
                                                                                            )
                    
                #Case of Frequency = Daily        
                if freq == "DAILY":
                    for ev in rrule.rrule(3, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter):
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
                #Case of Frequency = Weekly            
                if freq == "WEEKLY":
                    L=[i.week_day for i in event_form.cleaned_data['repeat_on']]
                    T=tuple([dicto[i] for i in L])
                    for ev in rrule.rrule(2, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=T):
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
                #Case of Frequency = Monthly
                if freq == "MONTHLY":
                    mo_rpt_day=dicto[event_form.cleaned_data['ordinal_day']](int(event_form.cleaned_data['ordinal']),)
                    for ev in rrule.rrule(1, dtstart=event_form.cleaned_data['date_started'], until=event_form.cleaned_data['date_completed'], interval=inter, byweekday=mo_rpt_day):
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
#            performance_obj, created = PerformanceDetails.objects.get_or_create(
#                                                          ticket_price = event_form.cleaned_data['event_ticket_price'],
#                                                          date_started = event_form.cleaned_data['date_started'],
#                                                          date_completed = event_form.cleaned_data['date_completed'],                  
#                                                          event = event_obj,
#                                                          place = place_obj,
#                                                          frequency = event_form.cleaned_data['frequency'],
#                                                          interval = event_form.cleaned_data['interval'],
#                                                          showtimes_start = event_form.cleaned_data['event_start_hours'], 
#                                                          showtimes_end = event_form.cleaned_data['event_end_hours'],                 
#                                                          )
#            
            for days in event_form.cleaned_data['repeat_on']:
                event_obj.by_day.add(days.id)
            for genre in event_form.cleaned_data['event_genre']:
                event_obj.event_genre.add(genre.id)
            for public in event_form.cleaned_data['event_public']:
                event_obj.event_public.add(public.id)
            try:
                old_event_obj.delete()
            except:
                pass
            return HttpResponseRedirect('/myprofile/home/')
            
        else:
            print "Form is not valid"
            
    else:
        event_form = EventForm()
        eventposter_form = EventPosterForm()
        event_poster = ""
        try:
            id = request.GET['id']
            event_obj = Event.objects.get(id=id)
            event_form.fields['title'].initial = event_obj.title
            #eventposter_form.fields['event_poster_file'].initial = event_obj.event_poster
            event_form.fields['eventwebsite'].initial = event_obj.eventwebsite
            event_form.fields['description'].initial = event_obj.description
            event_form.fields['venue_name'].initial = event_obj.location
            event_form.fields['category'].initial = event_obj.category
            event_form.fields['schedule_type'].initial = event_obj.schedule_type
            event_form.fields['street_address'].initial = event_obj.location
            event_form.fields['date_started'].initial = event_obj.event_start_date
            event_form.fields['date_completed'].initial = event_obj.event_completion_date
            
            # For Performance Based
            if event_form.fields['schedule_type'].initial == "performance_based":
                # ----1
                
                if event_obj.performancedetails_set.values('showtimes_start')[0].get('showtimes_start'):
                    event_form.fields['event_start_hours_1'].initial = event_obj.performancedetails_set.values('showtimes_start')[0].get('showtimes_start')
                    event_form.fields['event_end_hours_1'].initial = event_obj.performancedetails_set.values('showtimes_end')[0].get('showtimes_end')
                    event_form.fields['event_ticket_price_1'].initial = event_obj.performancedetails_set.values('ticket_price')[0].get('ticket_price')
                
                # ----2
                if event_obj.performancedetails_set.values('showtimes_start')[1].get('showtimes_start'):
                    event_form.fields['event_start_hours_2'].initial = event_obj.performancedetails_set.values('showtimes_start')[1].get('showtimes_start')
                    event_form.fields['event_end_hours_2'].initial = event_obj.performancedetails_set.values('showtimes_end')[1].get('showtimes_end')
                    event_form.fields['event_ticket_price_2'].initial = event_obj.performancedetails_set.values('ticket_price')[1].get('ticket_price')
                
                # ----3
                if event_obj.performancedetails_set.values('showtimes_start')[2].get('showtimes_start'):
                    event_form.fields['event_start_hours_3'].initial = event_obj.performancedetails_set.values('showtimes_start')[2].get('showtimes_start')
                    event_form.fields['event_end_hours_3'].initial = event_obj.performancedetails_set.values('showtimes_end')[2].get('showtimes_end')
                    event_form.fields['event_ticket_price_3'].initial = event_obj.performancedetails_set.values('ticket_price')[2].get('ticket_price')
                
                event_form.fields['frequency'].initial = event_obj.frequency
                event_form.fields['interval'].initial = event_obj.interval
                event_form.fields['repeat_on'].initial = [days for days in event_obj.by_day.all()]
                
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
                               'event_poster':event_poster
                               },
                              context_instance=RequestContext(request)
                              )
    

def home(request):
    category = Category.objects.all()
    return render_to_response("event/home_page.html",
                              {
                               "request":request,
                               "category":category
                               },
                              context_instance=RequestContext(request)
                              )

def handle_uploaded_file(request):
    event_poster = request.FILES['event_poster_file']
    
    import PIL
    from PIL import Image
    from cStringIO import StringIO
    from django.core.files.uploadedfile import InMemoryUploadedFile
    
    poster_wip = Image.open(event_poster)
    
    maxSize=(150,200)
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


def event_list(request):
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
    try:
        if request.GET['event_date']:
            event_date = request.GET['event_date'];
    except:
        pass
    
    try:
        if request.GET['event_date_end']:
            event_date_end = request.GET['event_date_end'];
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
        
        events = Event.objects.filter((Q(**kwargs1)|Q(**kwargs2))&start_time_q&end_time_q&searchbox_q&Q(**kwargs)&category_q&audience_q).distinct()
        #If view requested is 'by category'
    
    if (request.GET['tgl']!="0"):

        events_mov=events.filter(category=1).order_by("event_start_date")
        events_exh=events.filter(category=2).order_by("event_start_date")
        events_lec=events.filter(category=3).order_by("event_start_date")
        events_con=events.filter(category=4).order_by("event_start_date")
        events_spo=events.filter(category=5).order_by("event_start_date")
        events_the=events.filter(category=6).order_by("event_start_date")
        events_ope=events.filter(category=7).order_by("event_start_date")
        events_dan=events.filter(category=8).order_by("event_start_date")
        events_mus=events.filter(category=9).order_by("event_start_date")
        events_out=events.filter(category=10).order_by("event_start_date")
        events_fes=events.filter(category=11).order_by("event_start_date")
        events_sta=events.filter(category=12).order_by("event_start_date")
        events_cou=events.filter(category=13).order_by("event_start_date")
        events_cit=events.filter(category=14).order_by("event_start_date")
        events_fai=events.filter(category=15).order_by("event_start_date")
        events_fun=events.filter(category=16).order_by("event_start_date")
        events_par=events.filter(category=17).order_by("event_start_date")

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
                           },
                          context_instance=RequestContext(request)
                          ) 
    else:
        return render_to_response("event/event_list.html",
                           {
                           "request":request,
                           "events":events,
                           },
                          context_instance=RequestContext(request)
                          )
     
#        return render_to_response("event/event_list_cat.html",
#                               {
#                               "request":request,
#                               "events":events,
#                               },
#                              context_instance=RequestContext(request)
#                              ) 
    

def get_event_genre(request):  
    type = request.GET['type']
    category_obj = Category.objects.get(id=type)
    return render_to_response("event/event_genre.html",
                             {"genre_list":category_obj.eventgenre_set.all()},
                             context_instance=RequestContext(request)
                             )
    
def calendar(request):
    import datetime
    import dateutil
    from dateutil.relativedelta import *
    from calendar import monthrange
    
    now = datetime.datetime.now()
    
    try:
        current_date = datetime.datetime(int(request.GET["year"]),int(request.GET["month"]),1)
    except:
        current_date = datetime.datetime(int(now.year),int(now.month),1)
        
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
                                "now":now
                            },
                             context_instance=RequestContext(request)
                             )
       
def get_event_details(request):
    id = request.GET['id']
    event_obj = Event.objects.get(id=id)
    by_day = {}
    if event_obj.schedule_type == "open_hour_based":
        if event_obj.start_hours_on_monday and event_obj.end_hours_on_monday:
            by_day["Mon"] = {"start":event_obj.start_hours_on_monday,"end":event_obj.end_hours_on_monday}
        if event_obj.start_hours_on_tuesday and event_obj.end_hours_on_tuesday:
            by_day["Tues"] = {"start":event_obj.start_hours_on_tuesday,"end":event_obj.end_hours_on_tuesday}
        if event_obj.start_hours_on_wednesday and event_obj.end_hours_on_wednesday:
           by_day["Wed"] = {"start":event_obj.start_hours_on_wednesday,"end":event_obj.end_hours_on_wednesday}
        if event_obj.start_hours_on_thursday and event_obj.end_hours_on_thursday:
           by_day["Thu"] = {"start":event_obj.start_hours_on_thursday,"end":event_obj.end_hours_on_thursday}
        if event_obj.start_hours_on_friday and event_obj.end_hours_on_friday:
            by_day["Fri"] = {"start":event_obj.start_hours_on_friday,"end":event_obj.end_hours_on_friday}
        if event_obj.start_hours_on_saturday and event_obj.end_hours_on_saturday:
            by_day["Sat"] = {"start":event_obj.start_hours_on_saturday,"end":event_obj.end_hours_on_saturday}
        if event_obj.start_hours_on_sunday and event_obj.end_hours_on_sunday:
            by_day["Sun"] = {"start":event_obj.start_hours_on_sunday,"end":event_obj.end_hours_on_sunday}
                  
       
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
                        total_days_consecutive+=1
                except:
                    pass
    
    return render_to_response("event/event_detail.html",
                              {
                              # whatever you need from event table just do event_obj.fieldname in template
                               "eventdetails":event_obj,
                              # for performance details just iterate it in templates and access the value by using . notation
                              "event_performance":event_obj.performancedetails_set.all(),
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
                              },
                              context_instance=RequestContext(request)
                              )

def update_city(request):
    city = request.GET['city']
    request.session['city'] = city
    return HttpResponse(str(city))

def comment_delete(request):
    comment_id = request.GET['id']
    comment_obj = UserComments.objects.get(id=comment_id)
    comment_obj.delete()
    
    event_id = request.GET['event_id']
    return HttpResponseRedirect('/event/details/?id='+event_id)
    