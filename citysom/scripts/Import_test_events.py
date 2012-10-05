# Python Imports
import csv
import os
import sys
import datetime
import dateutil
from datetime import datetime
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
		days = row[34].split()
		days1 = row[39].split()
		days2 = row[44].split()
		days3 = row[49].split()
		days4 = row[54].split()
		days_list= []
		days_list1= []
		days_list2= []
		days_list3= []
		days_list4= []
		for d in days1:
		    if "MO" in d:
		        days_list1.append("1")
		    elif "FR" in d:
		    	days_list1.append("5")
		    elif "SA" in d:
		    	days_list1.append("6")
		    elif "SU" in d:
	        	days_list1.append("7")
		    elif "TU" in d:
		        days_list1.append("2")
		    elif "WE" in d:
		        days_list1.append("3")
		    elif "TH" in d:
	        	days_list1.append("4")
		
		for d in days2:
		    if "MO" in d:
		        days_list2.append("1")
		    elif "FR" in d:
		    	days_list2.append("5")
		    elif "SA" in d:
		    	days_list2.append("6")
		    elif "SU" in d:
	        	days_list2.append("7")
		    elif "TU" in d:
		        days_list2.append("2")
		    elif "WE" in d:
		        days_list2.append("3")
		    elif "TH" in d:
	        	days_list2.append("4")
		
		for d in days3:
		    if "MO" in d:
		        days_list3.append("1")
		    elif "FR" in d:
		    	days_list3.append("5")
		    elif "SA" in d:
		    	days_list3.append("6")
		    elif "SU" in d:
	        	days_list3.append("7")
		    elif "TU" in d:
		        days_list3.append("2")
		    elif "WE" in d:
		        days_list3.append("3")
		    elif "TH" in d:
	        	days_list3.append("4")
		
		for d in days4:
		    if "MO" in d:
		        days_list4.append("1")
		    elif "FR" in d:
		    	days_list4.append("5")
		    elif "SA" in d:
		    	days_list4.append("6")
		    elif "SU" in d:
	        	days_list4.append("7")
		    elif "TU" in d:
		        days_list4.append("2")
		    elif "WE" in d:
		        days_list4.append("3")
		    elif "TH" in d:
	        	days_list4.append("4")
	        	
		for d in days:
		    if "MO" in d:
		        days_list.append("1")
		    elif "FR" in d:
		    	days_list.append("5")
		    elif "SA" in d:
		    	days_list.append("6")
		    elif "SU" in d:
	        	days_list.append("7")
		    elif "TU" in d:
		        days_list.append("2")
		    elif "WE" in d:
		        days_list.append("3")
		    elif "TH" in d:
	        	days_list.append("4")
	    
		
		old_event_start_date = datetime.strptime(row[20], '%d/%m/%Y')
		event_start_date = old_event_start_date.strftime('%Y-%m-%d')
		
		old_event_complete_date = datetime.strptime(row[21], "%d/%m/%Y")
		event_complete_date = old_event_complete_date.strftime('%Y-%m-%d')
		
		old_event_start_date1 = datetime.strptime(row[22], '%d/%m/%Y')
		event_start_date1 = old_event_start_date1.strftime('%Y-%m-%d')
		
		old_event_complete_date1 = datetime.strptime(row[23], "%d/%m/%Y")
		event_complete_date1 = old_event_complete_date.strftime('%Y-%m-%d')
		
		old_event_start_date2 = datetime.strptime(row[24], '%d/%m/%Y')
		event_start_date2 = old_event_start_date2.strftime('%Y-%m-%d')
		
		old_event_complete_date2 = datetime.strptime(row[25], "%d/%m/%Y")
		event_complete_date2 = old_event_complete_date2.strftime('%Y-%m-%d')
		
		old_event_start_date3 = datetime.strptime(row[26], '%d/%m/%Y')
		event_start_date3 = old_event_start_date3.strftime('%Y-%m-%d')
		
		old_event_complete_date3 = datetime.strptime(row[27], "%d/%m/%Y")
		event_complete_date3 = old_event_complete_date3.strftime('%Y-%m-%d')
		
		old_event_start_date4 = datetime.strptime(row[28], '%d/%m/%Y')
		event_start_date4 = old_event_start_date4.strftime('%Y-%m-%d')
		
		old_event_complete_date4 = datetime.strptime(row[29], "%d/%m/%Y")
		event_complete_date4 = old_event_complete_date4.strftime('%Y-%m-%d')
		
		old_event_start_date5 = datetime.strptime(row[30], '%d/%m/%Y')
		event_start_date5 = old_event_start_date5.strftime('%Y-%m-%d')
		
		old_event_complete_date5 = datetime.strptime(row[31], "%d/%m/%Y")
		event_complete_date5 = old_event_complete_date5.strftime('%Y-%m-%d')
		
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
														event_completion_date=event_complete_date,\
														event_start_date1 = event_start_date1,\
														event_completion_date1=event_complete_date1,\
														event_start_date2 = event_start_date2,\
														event_completion_date2=event_complete_date2,\
														event_start_date3 = event_start_date3,\
														event_completion_date3=event_complete_date3,\
														event_start_date4 = event_start_date4,\
														event_completion_date4=event_complete_date4,\
														event_start_date5 = event_start_date5,\
														event_completion_date5=event_complete_date5,\
														frequency = row[32],\
														interval = row[33].strip('.0'),\
														
														by_monthday = row[34],\
														by_month = row[35],
														frequency1= row[37],\
														interval1=row[38].strip('.0'),\
														
														by_monthday1 = row[40],\
														by_month1=row[41],
														frequency2= row[42],\
														interval2=row[43].strip('.0'),\
														
														by_monthday2 = row[-12],\
														by_month2=row[-11],
														frequency3= row[-10],\
														interval3=row[-9].strip('.0'),\
														
														by_monthday3 = row[-7],\
														by_month3= row[-6],
														frequency4= row[-5],\
														interval4=row[-4].strip('.0'),\
														
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
		curr_event.event_genre.add(curr_genre.id)
		curr_event.event_public.add(curr_audience.id)
		for days in days_list:
			curr_event.by_day.add(days)
		for days1 in days_list1:
			curr_event.by_day1.add(days1)
		for days2 in days_list:
			curr_event.by_day2.add(days2)
		for days3 in days_list3:
			curr_event.by_day3.add(days3)
		for days4 in days_list4:
			curr_event.by_day4.add(days4)
			
				