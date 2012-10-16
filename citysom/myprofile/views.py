# Create your views here.
from citysom.myprofile.forms import UserProfileForm, EditUserProfileForm,\
PreRegistrationForm, PersonalProfileForm, ProfessionalProfileForm, AccountForm
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.contrib.auth.models import User
from citysom import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, load_backend
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from citysom.myprofile.models import Wishlist, History, Popularity, UserProfile
from citysom.event.models import Event, PerformanceDetails
import logging
logger = logging.getLogger("myprofile.views")
from django.template import loader
from django.core.mail import send_mail


def get_account_type(request):
    """
    separating the account_type
    """
    context=RequestContext(request)
    if request.method == "POST":
        account_form = PreRegistrationForm(request.POST)
        if account_form.is_valid():
            account_type = account_form.cleaned_data['account_type']
            acc_type = request.POST['account_type']
            userprofile_obj = UserProfile.objects.get(user=request.user)
            userprofile_obj.account_type = acc_type
            userprofile_obj.save()
            
            next_url = "/myprofile/completingprofile/"
            return HttpResponseRedirect(next_url)
    else:
        account_form = PreRegistrationForm()
        
    return render_to_response(
                              "myprofile/account_type.html",
                              {'account_form':account_form},
                              context_instance=context
                              )

###############################################################################
def completingprofile(request):
    """
    On the basis of account type you need to display the form
    """
    userprofile_obj = UserProfile.objects.get(user=request.user)
    if userprofile_obj.account_type == "personal":
        if request.method == "POST":
            form = PersonalProfileForm(request.POST)
            if form.is_valid():
                userprofile_obj.first_name = form.cleaned_data['first_name']
                userprofile_obj.last_name = form.cleaned_data['last_name']
                userprofile_obj.gender = form.cleaned_data['gender']
                userprofile_obj.mobile = form.cleaned_data['mobile']
                userprofile_obj.email_id_2 = form.cleaned_data['email2']
                userprofile_obj.email_id_3 = form.cleaned_data['email3']
                userprofile_obj.email_id_4 = form.cleaned_data['email4']
                userprofile_obj.facebook_account = form.cleaned_data['facebook_account']
                userprofile_obj.save()
                next_url = "http://"+settings.HOST
                request.session['message'] = "Your Profile has been successfully updated"
                return HttpResponseRedirect("/myprofile/editprofile/")
        else:
            form = PersonalProfileForm()
            
        return render_to_response(
                                  "myprofile/personal_profile_page.html",
                                  {'form':form},
                                  context_instance=RequestContext(request)
                                  )
    else:
        if request.method == "POST":
            form = ProfessionalProfileForm(request.POST)
            if form.is_valid():               
                userprofile_obj.first_name = form.cleaned_data['first_name']
                userprofile_obj.last_name = form.cleaned_data['last_name']
                userprofile_obj.gender = form.cleaned_data['gender']
                userprofile_obj.mobile = form.cleaned_data['mobile']
                userprofile_obj.institution_name = form.cleaned_data['institution_name']
                userprofile_obj.institution_website = form.cleaned_data['institution_website']
                userprofile_obj.street = form.cleaned_data['street']
                userprofile_obj.state = form.cleaned_data['state']
                userprofile_obj.zip_code = form.cleaned_data['zip_code']
                userprofile_obj.country = form.cleaned_data['country']
                userprofile_obj.start_hours_on_monday = form.cleaned_data['start_hours_on_monday']
                userprofile_obj.end_hours_on_monday = form.cleaned_data['end_hours_on_monday']
                userprofile_obj.start_hours_on_tuesday = form.cleaned_data['start_hours_on_tuesday']
                userprofile_obj.end_hours_on_tuesday = form.cleaned_data['end_hours_on_tuesday']
                userprofile_obj.start_hours_on_wednesday = form.cleaned_data['start_hours_on_wednesday']
                userprofile_obj.end_hours_on_wednesday = form.cleaned_data['end_hours_on_wednesday']
                userprofile_obj.start_hours_on_thursday = form.cleaned_data['start_hours_on_thursday']
                userprofile_obj.end_hours_on_thursday = form.cleaned_data['end_hours_on_thursday']
                userprofile_obj.start_hours_on_friday = form.cleaned_data['start_hours_on_friday']
                userprofile_obj.end_hours_on_friday = form.cleaned_data['end_hours_on_friday']
                userprofile_obj.start_hours_on_saturday = form.cleaned_data['start_hours_on_saturday']
                userprofile_obj.end_hours_on_saturday = form.cleaned_data['end_hours_on_saturday']
                userprofile_obj.start_hours_on_sunday = form.cleaned_data['start_hours_on_sunday']
                userprofile_obj.end_hours_on_sunday = form.cleaned_data['end_hours_on_sunday']
                userprofile_obj.save()
                request.session['message'] = "Your Profile has been successfully updated"
                return HttpResponseRedirect("/myprofile/editprofile/")
        else:
            form = ProfessionalProfileForm()   
        return render_to_response(
                                  "myprofile/professional_profile_page.html",
                                  {'form':form},
                                  context_instance=RequestContext(request)
                                  )
        
###############################################################################
def editprofile(request):
    """
    Creating a different function so that further customization
    remains easy and clear
    """
    context=RequestContext(request)
    userprofile_obj = UserProfile.objects.get(user=request.user)
    if userprofile_obj.account_type == "personal":
        context['form']= EditUserProfileForm()
        user = request.user
        profile=request.user.get_profile()
        context['form'].fields['first_name'].initial = profile.first_name
        context['form'].fields['last_name'].initial = profile.last_name
        context['form'].fields['gender'].initial = profile.gender
        context['form'].fields['mobile'].initial = profile.mobile
        
        context['form'].fields['email_id_2'].initial = profile.email_id_2
        context['form'].fields['email_id_3'].initial = profile.email_id_3
        context['form'].fields['email_id_4'].initial = profile.email_id_4
        context['form'].fields['facebook_account'].initial = profile.facebook_account
    elif userprofile_obj.account_type == "professional":
        context['form'] = ProfessionalProfileForm()
        user = request.user
        
        profile=request.user.get_profile()
        context['form'].fields['first_name'].initial = profile.first_name
        context['form'].fields['last_name'].initial = profile.last_name
        context['form'].fields['gender'].initial = profile.gender
        context['form'].fields['mobile'].initial = profile.mobile
        context['form'].fields['institution_name'].initial = profile.institution_name
        context['form'].fields['street'].initial = profile.street 
        context['form'].fields['zip_code'].initial = profile.zip_code
        context['form'].fields['state'].initial = profile.state
        context['form'].fields['country'].initial = profile.country
        context['form'].fields['institution_website'].initial = profile.institution_website
        context['form'].fields['start_hours_on_monday'].initial = profile.start_hours_on_monday
        context['form'].fields['end_hours_on_monday'].initial = profile.end_hours_on_monday
        context['form'].fields['start_hours_on_tuesday'].initial = profile.start_hours_on_tuesday
        context['form'].fields['end_hours_on_tuesday'].initial = profile.end_hours_on_tuesday
        context['form'].fields['start_hours_on_wednesday'].initial = profile.start_hours_on_wednesday
        context['form'].fields['end_hours_on_wednesday'].initial = profile.end_hours_on_wednesday
        context['form'].fields['start_hours_on_thursday'].initial = profile.start_hours_on_thursday
        context['form'].fields['end_hours_on_thursday'].initial = profile.end_hours_on_thursday
        context['form'].fields['start_hours_on_friday'].initial = profile.start_hours_on_friday
        context['form'].fields['end_hours_on_friday'].initial = profile.end_hours_on_friday
        context['form'].fields['start_hours_on_saturday'].initial = profile.start_hours_on_saturday
        context['form'].fields['end_hours_on_saturday'].initial = profile.end_hours_on_saturday
        context['form'].fields['end_hours_on_sunday'].initial = profile.end_hours_on_sunday
        context['form'].fields['start_hours_on_sunday'].initial = profile.start_hours_on_sunday
        
        context['account_type'] = profile.account_type
    
    else:    
        userprofile_obj = UserProfile.objects.get(user=request.user)
        context['form']= EditUserProfileForm()
        user = request.user
        profile=request.user.get_profile()
        context['form'].fields['first_name'].initial = profile.first_name
        context['form'].fields['last_name'].initial = profile.last_name
        context['form'].fields['gender'].initial = profile.gender
        context['form'].fields['mobile'].initial = profile.mobile
        
        context['form'].fields['email_id_2'].initial = profile.email_id_2
        context['form'].fields['email_id_3'].initial = profile.email_id_3
        context['form'].fields['email_id_4'].initial = profile.email_id_4
        context['form'].fields['facebook_account'].initial = profile.facebook_account

        context['account_type'] = profile.account_type 
        print context['account_type']   
    return render_to_response(
                              "myprofile/edit_profile_page.html",
                              {'account_type':userprofile_obj.account_type},
                               context_instance=context
                              )
###############################################################################

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                if user.get_profile().first_name != "":
                    return_str = user.get_profile().first_name + " " + user.get_profile().last_name
                else:
                    return_str = user.username
                return HttpResponse(return_str)
            else:
               return  HttpResponse('disabled')
        else:
           return  HttpResponse('invalid')
    else:
        return HttpResponseNotAllowed(['POST'])

###############################################################################

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse("1")
    else:
        return HttpResponseNotAllowed(['POST'])
###############################################################################            

def user_events(request):
    """
    Creating the view that lists the events a professional user has published
    and Personal user have added to their "wish list"
    """
    
    context=RequestContext(request)
    userprofile_obj = UserProfile.objects.get(user=request.user)
    if userprofile_obj.account_type == "personal":
        pass
#        context['form']= EditUserProfileForm()
#        user = request.user
#        profile=request.user.get_profile()
#        context['form'].fields['first_name'].initial = profile.first_name
#        context['form'].fields['last_name'].initial = profile.last_name
#        context['form'].fields['gender'].initial = profile.gender
#        context['form'].fields['mobile'].initial = profile.mobile
#        
#        context['form'].fields['email_id_2'].initial = profile.email_id_2
#        context['form'].fields['email_id_3'].initial = profile.email_id_3
#        context['form'].fields['email_id_4'].initial = profile.email_id_4
#        context['form'].fields['facebook_account'].initial = profile.facebook_account


    else:
        user = request.user
        
        user_events = Event.objects.filter(user=user).distinct().order_by('-id')
        events_performance_details = PerformanceDetails.objects.filter(event__user__exact=user)
        
    return render_to_response(
                              "myprofile/my_events.html",
                              {'account_type':userprofile_obj.account_type,
                               'events':user_events,
                               'pdet':events_performance_details,   
                               },
                               context_instance=context
                              )

###############################################################################
def wishlist(request):
    if request.GET['action'] == "add":
        event_id = request.GET['id']
        event = Event.objects.get(id=event_id)
        user = request.user
        wishlist_obj, created = Wishlist.objects.get_or_create(
                                                               event = event,
                                                               user = user
                                                               )
        request.session['message'] = "This event has been added to your Bookmarks. You can find it back in your profile page!"
        return HttpResponseRedirect("/event/details?id="+event_id)
###############################################################################


def dashboard(request):
    context=RequestContext(request)
    user = request.user
    wishlist_events = Wishlist.objects.filter(user=user).order_by("-id")
    history_events = Event.objects.filter(user=user).filter(event_completion_date__lt = datetime.now()).order_by("-id").distinct()
    upcoming_events = Event.objects.filter(user=user).filter(event_start_date__gte = datetime.now()).order_by("-id").distinct()
    return render_to_response(
                                "myprofile/dashboard.html",
                                {
                                    'wishlist_events':wishlist_events,
                                    'history_events':history_events,
                                    'upcoming_events':upcoming_events
                                },
                                context_instance=context
                              )
###############################################################################

def invitation(request):
    context=RequestContext(request)
    if request.method == "POST":        
        if request.POST['action'] == "invitation":
            emails =  request.POST['emails']
            emails_content = request.POST['emails_content']
            msg = loader.render_to_string('myprofile/invitation.txt', {"email_content":emails_content})
            emails = emails.split(",")
            for email in emails:
                send_mail(
                    'Citysom: Invitation' ,
                    msg,
                    'Citysom Event System <noreply@citysom.com>',
                    [email.strip()],
                    fail_silently=True
                )
            request.session['message'] = "Invitations sent successfully"
            return HttpResponseRedirect("/myprofile/invitation/")
    return render_to_response(
                                "myprofile/invitation.html",
                                {},
                                context_instance=context
                              )
###############################################################################

###############################################################################
def editaccount(request):
    """
        Edit Account Information
    """
    
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            user_obj = User.objects.get(username__exact=request.user)
            cd = form.cleaned_data
            user_obj.set_password(cd['password'])
            user_obj.save()
            request.session['message'] = "Your password has been successfully changed"
            return HttpResponseRedirect("/myprofile/editaccount/")
    else:
        form = AccountForm()
    
    return render_to_response(
                              "myprofile/edit_account_page.html",
                              {'form':form},
                               context_instance=RequestContext(request)
                              )
###############################################################################

###############################################################################
def popularity(request):
    if request.GET['action'] == "like" or request.GET['action'] == "unlike":
        event_id = request.GET['id']
        event = Event.objects.get(id=event_id)
        user = request.user
        
        popularity_events = Popularity.objects.filter(user=user).filter(event=event)
        if not popularity_events.count():
            if request.GET['action'] == "like":
                popularity = 1
            elif request.GET['action'] == "unlike":
                popularity = 0
            popularity_obj = Popularity.objects.get_or_create(
                                                                   event = event,
                                                                   user = user,
                                                                   popularity = popularity
                                                                   )
        popularity_count = Popularity.objects.filter(event=event)
        return HttpResponse(popularity_count.count())
###############################################################################
def login_user(request, user):
    """
    Log in a user without requiring credentials (using ``login`` from
    ``django.contrib.auth``, first finding a matching backend).

    """
    
    if not hasattr(user, 'backend'):
        for backend in settings.AUTHENTICATION_BACKENDS:
            if user == load_backend(backend).get_user(user.pk):
                user.backend = backend
                break
    if hasattr(user, 'backend'):
        return login(request, user)
    
###############################################################################

def registerfb(request):
        email = request.GET['email']
        first_name = request.GET['first_name']
        last_name = request.GET['last_name']
        gender = request.GET['gender']
        try:
            user = User.objects.get(username=email)
        except:
            user = User.objects.get_or_create(username=email,\
                                            first_name=first_name,
                                            last_name=last_name,
                                            password=""
                                            )
            user = user[0]
        login_user(request,user)
        return HttpResponseRedirect('/myprofile/home/')
    
###############################################################################