import csv
import os
import sys
import datetime
from datetime import datetime
import dateutil
import shutil
from operator import or_, and_
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
from citysom.settings import MEDIA_ROOT
# Django Imports
from django.contrib.auth.models import User
from django.db import connection
#Init environment, variables
file=sys.path[1] + '/page8.csv'
i=0
# Open the file in read mode
reader = csv.reader(open(file,'rb'))
#Creation de l'User
curr_user, created = User.objects.get_or_create(username="nikhilverma", is_staff=True, is_active=True, is_superuser=True)
curr_user.set_password("nikhil@123")
for row in reader:
	if i==0:
		i+=1
	
	else:
		curr_category, created = Category.objects.get_or_create(type=row[9])
		
		curr_genre, created = EventGenre.objects.get_or_create(genre_choices=row[10])
		curr_audience, created =EventPublic.objects.get_or_create(choicelist=row[11])
		#import pdb
		#pdb.set_trace()
		curr_place, created = Place.objects.get_or_create(venue_name=row[3], street=row[4],state=row[5])
		
		days = row[20].split(',')
		days1 = row[33].split(',')
		days2 = row[46].split(',')
		days3 = row[59].split(',')
		days4 = row[73].split(',')
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
			
		
		try:
			from datetime import *
			if row[14] != None:
				start_date_csv = datetime.strptime(row[14], '%d/%m/%Y')
				event_start_date = start_date_csv.strftime('%Y-%m-%d')
		except: 
			event_start_date = None
		try:
			from datetime import *
			if row[15] != None:
				complete_date_csv = datetime.strptime(row[15], '%d/%m/%Y')
				event_complete_date = complete_date_csv.strftime('%Y-%m-%d')
		except:
			event_complete_date = None
		try:
			from datetime import *
			if row[16] != None:
				start_date_csv1 = datetime.strptime(row[16], '%d/%m/%Y')
				event_start_date1 = start_date_csv1.strftime('%Y-%m-%d')
		except:
			event_start_date1 = None
		try:
			from datetime import *
			if row[17] != None:
				complete_date_csv1 = datetime.strptime(row[17], "%d/%m/%Y")
				event_complete_date1 = complete_date_csv1.strftime('%Y-%m-%d')
		except:
			event_complete_date1 = None
		try:
			from datetime import *
			if row[29] != None:
				start_date_csv2 = datetime.strptime(row[29], '%d/%m/%Y')
				event_start_date2 = start_date_csv2.strftime('%Y-%m-%d')
		except:
			event_start_date2 = None
		try:
			from datetime import *
			if row[30] != None:
				complete_date_csv2 = datetime.strptime(row[30], "%d/%m/%Y")
				event_complete_date2 = complete_date_csv2.strftime('%Y-%m-%d')
		except:
			event_complete_date2 = None
		try:
			from datetime import *
			if row[42] != None:
				start_date_csv3 = datetime.strptime(row[42], '%d/%m/%Y')
				event_start_date3 = start_date_csv3.strftime('%Y-%m-%d')
		except:
			event_start_date3 = None
		try:
			from datetime import *
			if row[43] != None:
				complete_date_csv3 = datetime.strptime(row[43], "%d/%m/%Y")
				event_complete_date3 = complete_date_csv3.strftime('%Y-%m-%d')
		except:
			event_complete_date3 = None
		try:
			from datetime import *
			if row[55] != None:
				start_date_csv4 = datetime.strptime(row[55], '%d/%m/%Y')
				event_start_date4 = start_date_csv4.strftime('%Y-%m-%d')
		except:
			event_start_date4 = None
		try:
			from datetime import *
			if row[56] != None:
				complete_date_csv4 = datetime.strptime(row[56], "%d/%m/%Y")
				event_complete_date4 = complete_date_csv4.strftime('%Y-%m-%d')
		except:
			event_complete_date4 = None
		try:
			from datetime import *
			if row[69] != None:
				start_date_csv5 = datetime.strptime(row[69], '%d/%m/%Y')
				event_start_date5 = start_date_csv5.strftime('%Y-%m-%d')
		except:
			event_start_date5 = None
		try:
			from datetime import *
			if row[70] != None:
				complete_date_csv5 = datetime.strptime(row[70], "%d/%m/%Y")
				event_complete_date5 = complete_date_csv5.strftime('%Y-%m-%d')
		except:
			event_complete_date5 = None

		try:
			if row[82] != None:
				start_hours_on_monday = row[82]
		except:
			start_hours_on_monday =None
		try:
			if row[83] != None:
				end_hours_on_monday = row[82]
		except:
			end_hours_on_monday = None
		
		try:
			if row[84] != None:
				start_hours_on_tuesday = row[84]
		except:
			start_hours_on_tuesday = None
		try:
			if row[85] != None:
				end_hours_on_tuesday = row[85]
		except:
			end_hours_on_tuesday = None
		
		try:
			if row[86] != None:
				start_hours_on_wednesday = row[86]
		except:
			start_hours_on_wednesday = None
		try:
			if row[87] != None:
				end_hours_on_wednesday = row[87]
		except:
			end_hours_on_wednesday = None
			
		try:
			if row[88] != None:
				start_hours_on_thursday = row[88]
		except:
			start_hours_on_thursday = None
		try:
			if row[89] != None:
				end_hours_on_thursday = row[89]
		except:
			end_hours_on_thursday = None
			
		try:
			if row[90] != None:
				start_hours_on_friday = row[90]
		except:
			start_hours_on_friday = None
		try:
			if row[91] != None:
				end_hours_on_friday = row[91]
		except:
			end_hours_on_friday = None
			
		
		try:
			if row[92] != None:
				start_hours_on_saturday = row[92]
		except:
			start_hours_on_saturday = None
		try:
			if row[93] != None:
				end_hours_on_saturday = row[93]
		except:
			end_hours_on_saturday = None
			
		try:
			if row[94] != None:
				start_hours_on_sunday = row[94]
		except:
			start_hours_on_sunday = None
		try:
			if row[95] != None:
				end_hours_on_sunday = row[95]
		except:
			end_hours_on_sunday = None
			
			
			
		#Variables used in all recurrences
		try:
			inter=int(row[19].strip('.0'))
			freq=row[18]
			dicto={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
		except:
			pass	
		try:
			inter1=int(row[32].strip('.0'))
			freq1=row[31]
			dicto1={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
		except:
			pass
		try:
			inter2=int(row[47].strip('.0'))
			freq2=row[44]
			dicto2={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
		except:
			pass
		try:	
			inter3=int(row[58].strip('.0'))
			freq3=row[57]
			dicto3={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
		except:
			pass
		try:	
			inter4=int(row[72].strip('.0'))
			freq4=row[71]
			dicto4={'Monday':rrule.MO, 'Tuesday': rrule.TU, 'Wednesday':rrule.WE, 'Thursday':rrule.TH, 'Friday':rrule.FR, 'Saturday':rrule.SA, 'Sunday':rrule.SU}
		except:
			pass	
		curr_event, created = Event.objects.get_or_create(title=row[1],\
								eventwebsite = row[12],
								description=row[7],\
								location=curr_place,\
								start_hours_on_monday = start_hours_on_monday or None,\
								end_hours_on_monday = end_hours_on_monday or None,\
								start_hours_on_tuesday = start_hours_on_tuesday or None,\
								end_hours_on_tuesday = end_hours_on_tuesday or None,\
								start_hours_on_wednesday = start_hours_on_wednesday or None,\
								end_hours_on_wednesday = end_hours_on_wednesday or None,\
								start_hours_on_thursday = start_hours_on_thursday or None,\
								end_hours_on_thursday = end_hours_on_thursday or None,\
								start_hours_on_friday = start_hours_on_friday or None,\
								end_hours_on_friday = end_hours_on_friday or None,\
								start_hours_on_saturday = start_hours_on_saturday or None,\
								end_hours_on_saturday = end_hours_on_saturday or None,\
								start_hours_on_sunday = start_hours_on_sunday or None,\
								end_hours_on_sunday = end_hours_on_sunday or None,\
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
								frequency = row[18],\
								interval = row[19].strip('.0'),\
								by_monthday = row[21],\
								by_month = row[22],
								frequency1= row[31],\
								interval1=row[32].strip('.0'),\
								by_monthday1 = row[34],\
								by_month1=row[35],
								frequency2= row[44],\
								interval2=row[45].strip('.0'),\
								by_monthday2 = row[47],\
								by_month2=row[48],
								frequency3= row[57],\
								interval3=row[58].strip('.0'),\
								by_monthday3 = row[60],\
								by_month3= row[61],
								frequency4= row[71],\
								interval4=row[72].strip('.0'),\
								by_monthday4 = row[74],\
								by_month4 = row[75],
								defaults={
								'user':curr_user,\
								'category':curr_category,\
								'event_poster':row[62],\
								'status':True,\
								'schedule_type':row[13]
								},
		
		)
		#Copy last uploaded image to 'images' directory
		try:
		    src= MEDIA_ROOT + '/images/tmp/'+ str(row[62])
		    dst= MEDIA_ROOT + '/images/'
		    shutil.move(src,dst)
		except:
		    pass
		curr_event.event_genre.add(curr_genre.id)
		curr_event.event_public.add(curr_audience.id)
		print days_list1,days_list2,days_list3,days_list4
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
		
		if row[13] == "performance_based":
		
			#Case of Frequency = Weekly            
			try:
				if freq == "WEEKLY":
					days = row[20].split(',')
					new_days_list = []
					for d in days:
						if "MO" in d:
						    new_days_list.append("Monday")
						if "FR" in d:
						    new_days_list.append("Friday")
						if "SA" in d:
						    new_days_list.append("Saturday")
						if "SU" in d:
						    new_days_list.append("Sunday")
						if "TU" in d:
						    new_days_list.append("Tuesday")
						if "WE" in d:
						    new_days_list.append("Wednesday")
						if "TH" in d:
						    new_days_list.append("Thursday")
					L=[i for i in new_days_list]
					
					T=tuple([dicto[i] for i in L])
					import datetime
					d_e = event_complete_date5.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date5.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=T):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[23]!= None and row[23] != "") and (row[24]!= None and row[24] != ""):
							sh_start=row[23] 
							sh_end=row[24]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
						#Test of Showtime 2
						if (row[25]!= None and row[25] != "") and (row[26]!= None and row[26] != ""):
							sh_start=row[25] 
							sh_end=row[26]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                    
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
						#Test of Showtime 3
						if (row[27]!= None and row[27] != "") and (row[28]!= None and row[28] != ""):
							sh_start=row[27] 
							sh_end=row[28]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
				if freq1 == "WEEKLY":
					days1 = row[33].split(',')
					new_days_list = []
					for d in days1:
						if "MO" in d:
						    new_days_list.append("Monday")
						if "FR" in d:
						    new_days_list.append("Friday")
						if "SA" in d:
						    new_days_list.append("Saturday")
						if "SU" in d:
						    new_days_list.append("Sunday")
						if "TU" in d:
						    new_days_list.append("Tuesday")
						if "WE" in d:
						    new_days_list.append("Wednesday")
						if "TH" in d:
						    new_days_list.append("Thursday")
					L=[i for i in new_days_list]
				
					T=tuple([dicto[i] for i in L])
					import datetime
					d_e = event_complete_date1.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date1.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter1, byweekday=T):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[36]!= None and row[36] != "") and (row[37]!= None and row[37] != ""):
							sh_start= row[36]
							sh_end=row[37]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
						#Test of Showtime 2
						if (row[38]!= None and row[38] != "") and (row[39]!= None and row[39] != ""):
							sh_start=row[38]
							sh_end=row[39]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
						#Test of Showtime 3
						if (row[40]!= None and row[40] != "") and (row[41]!= None and row[41] != ""):
							sh_start=row[40] 
							sh_end=row[41]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
					#Case of Frequency2 = Weekly
					if freq2 == "WEEKLY":
						days2 = row[46].split(',')
						new_days_list = []
						for d in days2:
							if "MO" in d:
							    new_days_list.append("Monday")
							if "FR" in d:
							    new_days_list.append("Friday")
							if "SA" in d:
							    new_days_list.append("Saturday")
							if "SU" in d:
							    new_days_list.append("Sunday")
							if "TU" in d:
							    new_days_list.append("Tuesday")
							if "WE" in d:
							    new_days_list.append("Wednesday")
							if "TH" in d:
							    new_days_list.append("Thursday")
					L=[i for i in new_days_list]
				
					T=tuple([dicto[i] for i in L])
					import datetime
					d_e = event_complete_date2.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date2.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter2, byweekday=T):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[49]!= None and row[49] != "") and (row[50]!= None and row[50] != ""):
							sh_start= row[49]
							sh_end=row[50]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
						#Test of Showtime 2
						if (row[51]!= None and row[51] != "") and (row[52]!= None and row[52] != ""):
							sh_start=row[51]
							sh_end=row[52]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
						#Test of Showtime 3
						if (row[53]!= None and row[53] != "") and (row[54]!= None and row[54] != ""):
							sh_start=row[53] 
							sh_end=row[54]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
													ticket_price = tix_price,
													date_of_performance = date_show,                  
													event = curr_event,
													place = curr_place,
													showtimes_start = sh_start, 
													showtimes_end = sh_end,
													)
				
					if freq3 == "WEEKLY":
						
						days3 = row[58].split(',')
						new_days_list = []
						for d in days3:
							if "MO" in d:
							    new_days_list.append("Monday")
							if "FR" in d:
							    new_days_list.append("Friday")
							if "SA" in d:
							    new_days_list.append("Saturday")
							if "SU" in d:
							    new_days_list.append("Sunday")
							if "TU" in d:
							    new_days_list.append("Tuesday")
							if "WE" in d:
							    new_days_list.append("Wednesday")
							if "TH" in d:
							    new_days_list.append("Thursday")
					L=[i for i in new_days_list]
				
					T=tuple([dicto[i] for i in L])
					import datetime
					d_e = event_complete_date3.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date3.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter3, byweekday=T):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[63]!= None and row[63] != "") and (row[64]!= None and row[64] != ""):
							sh_start= row[63]
							sh_end=row[64]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
						#Test of Showtime 2
						if (row[65]!= None and row[65] != "") and (row[66]!= None and row[66] != ""):
							sh_start=row[65]
							sh_end=row[66]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
						#Test of Showtime 3
						if (row[67]!= None and row[67] != "") and (row[68]!= None and row[68] != ""):
							sh_start=row[67] 
							sh_end=row[68]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
					if freq4 == "WEEKLY":
						days4 = row[71].split(',')
						new_days_list = []
						for d in days4:
							if "MO" in d:
							    new_days_list.append("Monday")
							if "FR" in d:
							    new_days_list.append("Friday")
							if "SA" in d:
							    new_days_list.append("Saturday")
							if "SU" in d:
							    new_days_list.append("Sunday")
							if "TU" in d:
							    new_days_list.append("Tuesday")
							if "WE" in d:
							    new_days_list.append("Wednesday")
							if "TH" in d:
							    new_days_list.append("Thursday")
					L=[i for i in new_days_list]
				
					T=tuple([dicto[i] for i in L])
					import datetime
					d_e = event_complete_date4.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date4.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter4, byweekday=T):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[76]!= None and row[76] != "") and (row[77]!= None and row[77] != ""):
							sh_start= row[76]
							sh_end=row[77]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
						#Test of Showtime 2
						if (row[78]!= None and row[78] != "") and (row[79]!= None and row[79] != ""):
							sh_start=row[78]
							sh_end=row[79]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
						#Test of Showtime 3
						if (row[80]!= None and row[80] != "") and (row[81]!= None and row[81] != ""):
							sh_start=row[80] 
							sh_end=row[81]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
			except:
				pass
			try:
				if freq == 'DAILY':
					
					import datetime
					d_e = event_complete_date5.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date5.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(3, dtstart=date_start, until=date_end, interval=inter):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[23] != None and row[23] != "") and (row[24] != None and row[24]!= ""):
							sh_start=row[23] 
							sh_end=row[24]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
						#Test of Showtime 2
						if (row[25] != None and row[25] != "") and (row[26] != None and row[26]!= ""):
							sh_start=row[25] 
							sh_end=row[26]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
						#Test of Showtime 3
						if (row[27] != None and row[27] != "") and (row[28] != None and row[28]!= ""):
							sh_start=row[27] 
							sh_end=row[28]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = date_show,                  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,
												)
				print freq1,freq
				if freq1 == 'DAILY':
					import datetime
					d_e = event_complete_date1.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date1.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(3, dtstart=date_start, until=date_end, interval=inter1):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[36] != None and row[36] != "") and (row[37] != None and row[37]!= ""):
							sh_start= row[36]
							sh_end=row[37]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[38] != None and row[38] != "") and (row[39] != None and row[39]!= ""):
							sh_start=row[38]
							sh_end=row[39]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[40] != None and row[40] != "") and (row[41] != None and row[41]!= ""):
							sh_start=row[40] 
							sh_end=row[41]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
				if freq2 == 'DAILY':
					import datetime
					d_e = event_complete_date2.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date2.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(3, dtstart=date_start, until=date_end, interval=inter2):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[49] != None and row[49] != "") and (row[50] != None and row[50]!= ""):
							sh_start= row[49]
							sh_end=row[50]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[51] != None and row[51] != "") and (row[52] != None and row[52]!= ""):
							sh_start=row[51]
							sh_end=row[52]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[53] != None and row[53] != "") and (row[54] != None and row[54]!= ""):
							sh_start=row[53] 
							sh_end=row[54]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
				if freq3 == 'DAILY':
					import datetime
					d_e = event_complete_date3.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date3.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(3, dtstart=date_start, until=date_end, interval=inter3):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[63] != None and row[63] != "") and (row[64] != None and row[64]!= ""):
							sh_start= row[63]
							sh_end=row[64]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[65] != None and row[65] != "") and (row[66] != None and row[66]!= ""):
							sh_start=row[65]
							sh_end=row[66]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
					
						#Test of Showtime 3
						if (row[67] != None and row[67] != "") and (row[68] != None and row[68]!= ""):
							sh_start=row[67] 
							sh_end=row[68]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
			
				if freq4 == 'DAILY':
					import datetime
					d_e = event_complete_date4.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date4.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
					for ev in rrule.rrule(3, dtstart=date_start, until=date_end, interval=inter4):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[76] != None and row[76] != "") and (row[77] != None and row[77]!= ""):
							sh_start= row[76]
							sh_end=row[77]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[78] != None and row[78] != "") and (row[79] != None and row[79]!= ""):
			
							sh_start=row[78]
							sh_end=row[79]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[80] != None and row[80] != "") and (row[81] != None and row[81]!= ""):
							sh_start=row[80] 
							sh_end=row[81]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
			
			except:
				pass
			try:
				if freq == "ONCE":
					#Test of Showtime 1
					if (row[23] != None and row[23] != "") and (row[24] != None and row[24]!= ""):
						sh_start=row[23] 
						sh_end=row[24]
						tix_price=row[6]
						performance_obj, created = PerformanceDetails.objects.get_or_create(
												ticket_price = tix_price,
												date_of_performance = event_start_date5,					  
												event = curr_event,
												place = curr_place,
												showtimes_start = sh_start, 
												showtimes_end = sh_end,				 
												)
			
				if freq1 == "ONCE":
					#Test of Showtime 1 under frequency 1
					if (row[36]!= None and row[36] != "") and (row[37]!= None and row[37] != ""):
						sh_start= row[36]
						sh_end=row[37]
						tix_price=row[6]
						performance_obj, created = PerformanceDetails.objects.get_or_create(
												    ticket_price = tix_price,
												    date_of_performance = event_start_date1,				  
												    event = curr_event,
												    place = curr_place,
												    showtimes_start = sh_start, 
												    showtimes_end = sh_end,				 
												    )
				
				if freq2 == "ONCE":
					#Test of Showtime 1 under frequency 2
					if (row[42]!= None and row[42] != "") and (row[43]!= None and row[43] != ""):
						sh_start= row[49]
						sh_end=row[50]
						tix_price=row[6]
						performance_obj, created = PerformanceDetails.objects.get_or_create(
											ticket_price = tix_price,
											date_of_performance = event_start_date2,					  
											event = curr_event,
											place = curr_place,
											showtimes_start = sh_start, 
											showtimes_end = sh_end,
											)
			
				if freq3 == "ONCE":
					#Test of Showtime 1 under frequency 3
					if (row[63]!= None and row[63] != "") and (row[64]!= None and row[64] != ""):
						sh_start= row[63]
						sh_end=row[64]
						tix_price=row[6]
						performance_obj, created = PerformanceDetails.objects.get_or_create(
											ticket_price = tix_price,
											date_of_performance = event_start_date3,					  
											event = curr_event,
											place = curr_place,
											showtimes_start = sh_start, 
											showtimes_end = sh_end,				 
											)
						
				if freq4 == "ONCE":
					#Test of Showtime 1 under frequency 4
					if (row[80] != None) and (row[81] != None):
						sh_start= row[76]
						sh_end=row[77]
						tix_price=row[6]
						performance_obj, created = PerformanceDetails.objects.get_or_create(
											ticket_price = tix_price,
											date_of_performance = event_start_date4,					  
											event = curr_event,
											place = curr_place,
											showtimes_start = sh_start,
											showtimes_end = sh_end,
											)
			except:
				pass
			try:
				if freq == "MONTHLY":
					import datetime
					d_e = event_complete_date5.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date5.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					mo_rpt_day=dicto[row[22]](int(row[21]),)
					for ev in rrule.rrule(1, dtstart=date_start, until=date_end, interval=inter, byweekday=mo_rpt_day):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
				
						if (row[23] != None and row[23] != "") and (row[24] != None and row[23] != ""):
							sh_start=row[23] 
							sh_end=row[24]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[25] != None and row[25] != "") and (row[26] != None and row[26] != ""):
							sh_start=row[25] 
							sh_end=row[26]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                    
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[27] != None and row[27] != "") and (row[28] != None and row[28] != ""):
							sh_start=row[27] 
							sh_end=row[28]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
				if freq1 == "MONTHLY":
					import datetime
					d_e = event_complete_date1.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date1.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					mo_rpt_day=dicto[row[35]](int(row[34]),)
					for ev in rrule.rrule(1, dtstart=date_start, until=date_end, interval=inter1, byweekday=mo_rpt_day):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[36] != None and row[36] != "") and (row[37] != None and row[37] != ""):
							sh_start= row[36]
							sh_end=row[37]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[38] != None and row[38] != "") and (row[39] != None and row[39] != ""):
							sh_start=row[38]
							sh_end=row[39]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[40] != None and row[40] != "") and (row[41] != None and row[41] != ""):
							sh_start=row[40]
							sh_end=row[41]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
				if freq2 == "MONTHLY":
					import datetime
					d_e = event_complete_date2.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date2.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					mo_rpt_day=dicto[row[48]](int(row[47]),)
					for ev in rrule.rrule(1, dtstart=date_start, until=date_end, interval=inter1, byweekday=mo_rpt_day):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[49] != None and row[49] != "") and (row[50] != None and row[50] != ""):
							sh_start= row[49]
							sh_end=row[50]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
											    ticket_price = tix_price,
											    date_of_performance = date_show,                  
											    event = curr_event,
											    place = curr_place,
											    showtimes_start = sh_start, 
											    showtimes_end = sh_end,
											    )
						#Test of Showtime 2
						if (row[51] != None and row[51] != "") and (row[52] != None and row[52] != ""):
							sh_start=row[51]
							sh_end=row[52]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[53] != None and row[53] != "") and (row[54] != None and row[54] != ""):
							sh_start=row[53] 
							sh_end=row[54]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
				if freq3 == "MONTHLY":
					import datetime
					d_e = event_complete_date3.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date3.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					mo_rpt_day=dicto[row[61]](int(row[60]),)
					for ev in rrule.rrule(1, dtstart=date_start, until=date_end, interval=inter1, byweekday=mo_rpt_day):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[63] != None and row[63] != "") and (row[64] != None and row[64] != ""):
							sh_start= row[63]
							sh_end=row[64]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[65] != None and row[65] != "") and (row[66] != None and row[66] != ""):
							sh_start=row[65]
							sh_end=row[66]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[67] != None and row[67] != "") and (row[68] != None and row[68] != ""):
							sh_start=row[67] 
							sh_end=row[68]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
				if freq4 == "MONTHLY":
					import datetime
					d_e = event_complete_date4.split("-")
					date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
					
					if date_end < datetime.date.today():
						pass
					else:
						d_s = event_start_date4.split('-')
						date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					mo_rpt_day=dicto[row[75]](int(row[74]),)
					for ev in rrule.rrule(1, dtstart=date_start, until=date_end, interval=inter1, byweekday=mo_rpt_day):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						#Test of Showtime 1
						if (row[76] != None and row[76] != "") and (row[77] != None and row[77] != ""):
							sh_start= row[76]
							sh_end=row[77]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 2
						if (row[78] != None and row[78] != "") and (row[79] != None and row[79] != ""):
							sh_start=row[78]
							sh_end=row[79]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
						#Test of Showtime 3
						if (row[80] != None and row[80] != "") and (row[81] != None and row[81] != ""):
							sh_start=row[80] 
							sh_end=row[81]
							tix_price=row[6]
							performance_obj, created = PerformanceDetails.objects.get_or_create(
															    ticket_price = tix_price,
															    date_of_performance = date_show,                  
															    event = curr_event,
															    place = curr_place,
															    showtimes_start = sh_start, 
															    showtimes_end = sh_end,
															    )
			
			except:
				pass
			
		elif row[13]  == "openhour_based":
			#Open Hour Based Performance Records
			import datetime
			
			try:
				d_e = event_complete_date.split("-")
				date_end = datetime.date(int(d_e[0]), int(d_e[1]), int(d_e[2]))
			
				if date_end < datetime.date.today():
					pass
				else:
					d_s = event_start_date.split('-')
					date_start = max(datetime.date(int(d_s[0]), int(d_s[1]), int(d_s[2])), datetime.date.today())
					
			except:
				pass
			
			try:
				if (row[82] != None and row[82] != "") and (row[83] != None and row[83] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.MO):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[82], 
										showtimes_end = row[83],
										)
			except:
				pass
			try:
				if (row[84] != None and row[84] != "") and (row[85] != None and row[85] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.TU):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[84], 
										showtimes_end = row[85],
										)
			except:
				pass
			try:
				if (row[86] != None and row[86] != "") and (row[87] != None and row[87] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.WE):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[86], 
										showtimes_end = row[87],
										)
			except:
				pass
			
			try:
				if (row[88] != None and row[88] != "") and (row[89] != None and row[89] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.TH):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[88], 
										showtimes_end = row[89],
										)
			except:
				pass
			
			try:
				if (row[90] != None and row[90] != "") and (row[91] != None and row[91] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.FR):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[90], 
										showtimes_end = row[91],
										)
			except:
				pass
			try:
				if (row[92] != None and row[92] != "") and (row[93] != None and row[93] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.SA):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[92], 
										showtimes_end = row[93],
										)
			except:
				pass
			try:
				if (row[94] != None and row[94] != "") and (row[95] != None and row[95] != ""):
					for ev in rrule.rrule(2, dtstart=date_start, until=date_end, interval=inter, byweekday=rrule.SU):
						date_show=str(ev.year)+'-'+str(ev.month)+'-'+str(ev.day)
						performance_obj, created = PerformanceDetails.objects.get_or_create(
										ticket_price = row[6],
										date_of_performance = date_show,                  
										event = curr_event,
										place = curr_place,
										showtimes_start = row[94], 
										showtimes_end = row[95],
										)
			except:
				pass
				
						
		else:
			pass
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
