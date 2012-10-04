# Python Imports
import csv
import os
import sys
import datetime
import dateutil
from dateutil import rrule
# Add the current directory to Python's system path.
cwd = os.path.split(os.getcwd())[0]
sys.path = [cwd+'/citysom'] + sys.path
# We need the Django settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citysom.settings")
# Citysom Imports
from citysom import settings
os.chdir(settings.PROJECT_PATH)
from citysom.event.models import Place, Event, Category,\
PerformanceDetails, EventGenre, EventPublic, Days
# Django Imports
from django.contrib.auth.models import User
from django.db import connection

#import pdb;pdb.set_trace();
#Init environment, variables
file=sys.path[1] + '/testing.csv'
i=0
# Open the file in read mode
reader = csv.reader(open(file,'rb'))
#Creation de l'User
curr_user, created = User.objects.get_or_create(username="nikhilverma", is_staff=True, is_active=True, is_superuser=True)
curr_user.set_password("nikhil@123")
for row in reader:
	print row
	if i==0:
		i+=1
		
	else:
		
		curr_category, created = Category.objects.get_or_create(type=row[16])
		
		curr_genre, created = EventGenre.objects.get_or_create(genre_choices=row[17])
		curr_audience, created =EventPublic.objects.get_or_create(choicelist=row[3])
		
		curr_place, created = Place.objects.get_or_create(venue_name=row[6], street=row[7], state=row[8])
		
		#curr_day, created = Days.objects.get_or_create(event_event_by_day=row[34])
		#from django.db import connection
		#connection.close()
		from datetime import datetime
		d = datetime.strptime(row[20], '%d/%m/%y')
		event_start_date = d.strftime('%Y-%m-%d')
		curr_event, created = Event.objects.get_or_create(title=row[0],\
														eventwebsite = row[9],
														description=row[4],\
														location=curr_place,\
#														start_hours_on_monday = row[1],\
#														end_hours_on_monday = row[2],\
#														start_hours_on_tuesday = row[3],\
#														end_hours_on_tuesday = row[4],\
#														start_hours_on_wednesday = row[5],\
#														end_hours_on_wednesday = row[6],\
#														start_hours_on_thursday = row[7],\
#														end_hours_on_thursday = row[8],\
#														start_hours_on_friday = row[9],\
#														end_hours_on_friday = row[10],\
#														start_hours_on_saturday = row[11],\
#														end_hours_on_saturday = row[12],\
#														start_hours_on_sunday = row[1],\
#														end_hours_on_sunday = row[2],\
														event_start_date = event_start_date,\
#														event_completion_date=row[21],\
#														event_start_date1 = row[22],\
#														event_completion_date1=row[23],\
#														event_start_date2 = row[24],\
#														event_completion_date2=row[25],\
#														event_start_date3 = row[26],\
#														event_completion_date3=row[27],\
#														event_start_date4 = row[28],\
#														event_completion_date4=row[29],\
#														event_start_date5 = row[30],\
#														event_completion_date5=row[31],\
														frequency = row[32],\
														interval = row[33].strip('.0'),\
#														#by_day=row[34],
														by_monthday = row[34],\
														by_month = row[35],
														frequency1= row[37],\
														interval1=row[38].strip('.0'),\
##														by_day1=row[38],\
														by_monthday1 = row[40],\
														by_month1=row[41],
														frequency2= row[42],\
														interval2=row[43].strip('.0'),\
##														by_day2 = row[42],\
														by_monthday2 = row[-12],\
														by_month2=row[-11],
														frequency3= row[-10],\
														interval3=row[-9].strip('.0'),\
##														by_day3=row[46],\
														by_monthday3 = row[-7],\
														by_month3= row[-6],
														frequency4= row[-5],\
														interval4=row[-4].strip('.0'),\
#														by_day4=row[50],\
														by_monthday4 = row[-2],\
														by_month4 = row[-1],
														defaults={
																'user':curr_user,\
																'category':curr_category,\
																'event_poster':row[19],\
																'status':True,\
																'schedule_type':row[47]
																},
														
														)
		#curr_event.event_genre=curr_genre
		#curr_event.event_public=curr_audience
		
		curr_event.event_genre.add(curr_genre.id)
		curr_event.event_public.add(curr_audience.id)
		curr_event.by_day.add(curr_day.id)


			
		