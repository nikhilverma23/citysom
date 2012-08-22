# Create your views here.
import sys
from citysom.event.models import Place, Event, Category, PerformanceDetails
from django.shortcuts import render_to_response
from django.template import RequestContext
from citysom.event.forms import EventForm, EventPosterForm
from django.http import Http404, HttpResponse,HttpResponseRedirect, HttpResponseServerError
from django.template import loader, Context
from django import http
from django.contrib.auth.decorators import login_required
from citysom.settings import MEDIA_ROOT,STATIC_ROOT
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
            place_obj = Place(
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
            place_obj.save()
            event_obj = Event(
            user = request.user,
            title = event_form.cleaned_data['title'],
           
            
            
            eventwebsite = event_form.cleaned_data['eventwebsite'],
            keyword = event_form.cleaned_data['keyword'],
            description = event_form.cleaned_data['description'],
            status = event_form.cleaned_data['status'],
            event_poster = event_form.cleaned_data['event_poster'],
            location = place_obj,
            category = event_form.cleaned_data['category'], 
            schedule_type = event_form.cleaned_data['schedule_type'],
            )
            event_obj.save()
            
            # Saving multiple Performance table object
            #import pdb;pdb.set_trace();
            from datetime import *
            from dateutil import rrule
            from dateutil.rrule import *
            from dateutil.parser import *
            
            # converting string date into datetime object to apply in rrule for date_started
            date_start = datetime.strptime(str(event_form.cleaned_data['date_started']), "%Y-%m-%d")
             # converting string date into datetime object to apply in rrule for date_completed
            date_comp = datetime.strptime(str(event_form.cleaned_data['date_completed']), "%Y-%m-%d")
            
            
            # Checking the value of DAILY parameter in rrule function
            # 1) on the basis of daily
            if event_form.cleaned_data['frequency'] == "DAILY":
                freq = DAILY
                # Now applying the rrule acc to dateutil documentation for daily
                daily_range = list(rrule(freq,interval=int(event_form.cleaned_data['interval']),\
                             dtstart=date_start,\
                             until=date_comp,\
                             )
                            )
                event_repeat = daily_range
            # 1) on the basis of weekly
            elif event_form.cleaned_data['frequency'] == "WEEKLY":
                freq = WEEKLY
                byweekday = event_form.cleaned_data['repeat_on']
                # We need parameter for weekly repeat on
                byweekday=tuple([days.id-1 for days in byweekday])
                
                # Now applying the rrule acc to dateutil documentation for weekly
                weekly_range = list(rrule(freq,interval=int(event_form.cleaned_data['interval']),\
                                 dtstart=date_start,\
                                 byweekday=tuple([days-1 for days in byweekday]),\
                                 until=date_comp,\
                                 )
                                )
                event_repeat = weekly_range
            # 3) on the basis of monthly
            elif event_form.cleaned_data['frequency'] == "MONTHLY":
                freq = MONTHLY
                # Now applying the rrule acc to dateutil documentation for monthly
                by_set_pos = int(event_form.cleaned_data['by_set_pos']) 
                byweekday = event_form.cleaned_data['byweekday']
                # TODO :- Improve this code make it in a form of dictionary
                # Doing this to satisfy the dateutil documentation
                if byweekday == "MO":
                    days_of_week = MO
                elif byweekday == "TU":
                    days_of_week = TU 
                elif byweekday == "WE":
                    days_of_week = WE
                elif byweekday == "TH":
                    days_of_week = TH
                elif byweekday == "FR":
                    days_of_week = FR
                elif byweekday == "SA":
                    days_of_week = SA
                elif byweekday == "SU":
                    days_of_week = SU 
                    
                # Now applying the rrule acc to dateutil documentation for monthly
                monthly_range = list(rrule(freq,interval=int(event_form.cleaned_data['interval']),\
                                 byweekday=(days_of_week(by_set_pos)),
                                 dtstart=date_start,\
                                 until=date_comp,\
                                 )
                                )
                event_repeat = monthly_range
            
            else:
                pass
            
            
            
            
            # list of tuples of show time starts and show time ends
            showtimes_start_option1 = event_form.cleaned_data['event_start_hours']
            showtimes_end_option1 = event_form.cleaned_data['event_end_hours']
            showtimes_start_option2 = event_form.cleaned_data['event_start_hours_option2']
            showtimes_end_option2 = event_form.cleaned_data['event_end_hours_option2']
            showtimes_start_option3 = event_form.cleaned_data['event_start_hours_option3']
            showtimes_end_option3 = event_form.cleaned_data['event_end_hours_option3']
            showtimes_start_option4 = event_form.cleaned_data['event_start_hours_option4']
            showtimes_end_option4 = event_form.cleaned_data['event_end_hours_option4']
            
            # Making store the mutiple time
            #TODO:- make this like a formset in html 
            # Do mot allow user to skip time hours by javascript            
            if not showtimes_start_option2 or showtimes_end_option2:
                multiple_times = [(showtimes_start_option1,showtimes_end_option1)]
            elif not showtimes_start_option3 or showtimes_end_option3: 
                multiple_times = [(showtimes_start_option1,showtimes_end_option1),(showtimes_start_option2,showtimes_end_option2)]
            
            elif not showtimes_start_4 or showtimes_end_option4: 
                multiple_times = [
                                  (showtimes_start_option1,showtimes_end_option1),(showtimes_start_option2,showtimes_end_option2),
                                  (showtimes_start_option3,showtimes_end_option3)
                                  ]
            else:
            
                multiple_times = [
                                  (showtimes_start_1,showtimes_end_1),(showtimes_start_2,showtimes_end_2)
                                  (showtimes_start_3,showtimes_end_3),(showtimes_start_4,showtimes_end_4)
                                  ]
                
            print multiple_times
            
            #for x in event_repeats:
            for repeat in event_repeat:
                if not showtimes_start_2 or showtimes_end_2:
                    multiple_times = [(showtimes_start_1,showtimes_end_1)]
                elif not showtimes_start_3 or showtimes_end_3: 
                    multiple_times = [(showtimes_start_1,showtimes_end_1),(showtimes_start_2,showtimes_end_2)]
                
                elif not showtimes_start_4 or showtimes_end_4: 
                    multiple_times = [
                                      (showtimes_start_1,showtimes_end_1),(showtimes_start_2,showtimes_end_2),
                                      (showtimes_start_3,showtimes_end_3)
                                      ]
                else:
                
                    multiple_times = [
                                      (showtimes_start_1,showtimes_end_1),(showtimes_start_2,showtimes_end_2)
                                      (showtimes_start_3,showtimes_end_3),(showtimes_start_4,showtimes_end_4)
                                      ]
                
                for times in multiple_times:
                    performance_obj = PerformanceDetails(
                                       ticket_price = event_form.cleaned_data['event_ticket_price'],
                                       date_started = repeat,
                                       date_completed = repeat,                  
                                       event = event_obj,
                                       place = place_obj,
                                       frequency = event_form.cleaned_data['frequency'],
                                       interval = event_form.cleaned_data['interval'],
                                       showtimes_start = times[0], 
                                       showtimes_end = times[1],                 
                                       )
                    performance_obj.save()
                
            for days in event_form.cleaned_data['repeat_on']:
                performance_obj.by_day.add(days.id)
            for genre in event_form.cleaned_data['event_genre']:
                event_obj.event_genre.add(genre.id)
            for public in event_form.cleaned_data['event_public']:
                event_obj.event_public.add(public.id)
            return HttpResponseRedirect('/myprofile/home/')
            
        else:
            print "Form is getting Invalid"
            
    else:
        
        eventposter_form = EventPosterForm()
        event_form = EventForm()
        
    frequency_range = {"daily":range(6),"weekly":range(4),"monthly":range(12)}
    return render_to_response('event/event.html',
                              {
                               'eventform':event_form,
                               'eventform_poster':eventposter_form,
                               'frequency_range':frequency_range
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
    destination = open(MEDIA_ROOT + '/images/'+ str(event_poster), 'wb+')
    for chunk in event_poster.chunks():
        destination.write(chunk)

    return HttpResponse(str(event_poster))

def event_list(request):
    kwargs = {
              'status':True,
             }
        
    try:
        if request.GET['event_date']:
            kwargs['performancedetails__date_started'] = request.GET['event_date']
    except:
        pass
    
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
        if request.GET['date_completed']:
            kwargs['performancedetails__date_completed'] = request.GET['date_completed']
    except:
        pass
    
    try:
        if request.GET['keyword']:
            kwargs['title__icontains'] = request.GET['keyword']
    except:
        pass
    
#    try:
#        if request.GET['start_time']:
#            kwargs['performancedetails__showtimes_start'] = request.GET['start_time']
#    except:
#        pass
    
    try:
        if request.GET['category']:
            kwargs['category'] = request.GET['category']
    except:
        pass
    
    events = Event.objects.filter(**kwargs)
    
    return render_to_response("event/event_list.html",
                               {
                               "request":request,
                               "events":events,
                               },
                              context_instance=RequestContext(request)
                              )    

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
        if request.user.is_authenticated():
            user = request.user
            history_obj = History(
                                event = event_obj,
                                user = user
                            )
            history_obj.save()
        
	return render_to_response("event/event_detail.html",
                              {
                              # whatever you need from event table just do event_obj.fieldname in template
                               "eventdetials":event_obj,
                              # for performance details just iterate it in templates and access the value by using . notation
                              "event_performance":event_obj.performancedetails_set.all(),
                              },
                              context_instance=RequestContext(request)
                              )
	    