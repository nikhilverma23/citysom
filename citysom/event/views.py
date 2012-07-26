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
            performance_obj = PerformanceDetails(
                               ticket_price = event_form.cleaned_data['event_ticket_price'],
                               date_started = event_form.cleaned_data['date_started'],
                               date_completed = event_form.cleaned_data['date_completed'],                  
                               event = event_obj,
                               place = place_obj,
                               frequency = event_form.cleaned_data['frequency'],
                               interval = event_form.cleaned_data['interval']
                                                 
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
        
        
    return render_to_response('event/event.html',
                              {'eventform':event_form,
                               'eventform_poster':eventposter_form},
                              context_instance=RequestContext(request)
                              )
def home(request):
    return render_to_response("event/home_page.html",
                              {"request":request},
                              context_instance=RequestContext(request)
                              )
    
def handle_uploaded_file(request):
    event_poster = request.FILES['event_poster_file']
    destination = open(STATIC_ROOT + '/images/'+ str(event_poster), 'wb+')
    for chunk in event_poster.chunks():
        destination.write(chunk)

    return HttpResponse(str(event_poster))

def event_list(request):
    kwargs = {
              'status':True,
             }
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
       