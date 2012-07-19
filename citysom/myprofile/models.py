from datetime import datetime
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import signals
from django.db import  models
from citysom.registration.signals import user_activated
from citysom.util import GENDER_CHOICES, ACCOUNT_TYPE
from django.contrib.admin import widgets 
from django.db.models.signals import post_save
from django.db.models import Q, signals
from django.db.utils import DatabaseError
import logging
logger = logging.getLogger("myprofile.models")

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=30,blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=15, blank=True)
    primary_email = models.EmailField(max_length=60, blank=True)
    account_type = models.CharField(max_length=80,
                                    choices=ACCOUNT_TYPE,
                                    null=True,blank=True
                                    )
    # For professional Account
    institution_name = models.CharField(max_length=100,blank=True,null=True)
    institution_website = models.CharField(max_length=100,blank=True,null=True)
    street = models.CharField(max_length=75)
    state = models.CharField(max_length=30)
    zip_code = models.IntegerField(max_length=7, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True)
   
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
    # For personal account form
    email_id_2 = models.EmailField(max_length=80,blank=True,null=True)
    email_id_3 = models.EmailField(max_length=80,blank=True,null=True)
    email_id_4 = models.EmailField(max_length=80,blank=True,null=True)
    facebook_account = models.URLField(max_length=80,blank=True,null=True)
       
    def __unicode(self):
        name = self.first_name + self.last_name
        return name
    

def user_post_save(sender,instance, signal, *args, **kwargs):
    # Creates user profile
    try:
        try:
            profile = instance.get_profile()
            logger.info("Existing user '%s'." % instance)
        except ObjectDoesNotExist:
            try:
                profile = UserProfile.objects.get(
                                            Q(primary_email=instance.email))
                logger.info("Profile found '%s', merging:: '%s'." % (profile,
                                                                     instance))
                profile.user = instance
            except Exception:
                profile = UserProfile(user=instance)
                profile.save()
                logger.info("Profile not found, creating new one '%s'." %
                            instance)
        
        profile.primary_email = instance.email
        profile.save()
    except DatabaseError:
        pass

signals.post_save.connect(user_post_save, User)



def user_pre_delete(sender, instance, *args, **kwargs):
    instance.get_profile().delete()

signals.pre_delete.connect(user_pre_delete, User)


def login_on_activation(sender, user, request, **kwargs):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    logger.info("Logged in user: '%s' after account activation." % user)

user_activated.connect(login_on_activation)