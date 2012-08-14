from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
        
	    ('mr', 'Mr'),
        ('mrs', 'Mrs'),
	    ('mis', 'Miss'),
	    ('ms', 'Ms'),
    )

ACCOUNT_TYPE = (
                
            ('personal','Personal'),    
            ('professional','Professional')
            )

EVENT_GENRE = (
                 
        ('classical','CLASSICAL'),
        ('rock','ROCK'),
        ('indie','INDIE'),
        ('comedy','COMEDY'),
        ('action','ACTION'),                 
)

EVENT_PUBLIC = (
                  
        ('children','CHILDREN'),
        ('all','ALL'),
        ('public','PUBLIC'),
        ('adults','ADULTS'),
        ('younger','YOUNGER'),
        ('older','OLDER'),
           
)
#
SCHEDULE_TYPE = (
    ('performance_based','Performance based (default)'),           
    ('open_hour_based','Open hour based'),
)

DAYS_OF_WEEK = (
               
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
    
)

FREQUENCY_CHOICES = (
                        ('once','Once'),
                        ('daily','Daily'),
                        ('weekly','Weekly'),
                        ('monthly','Monthly'),
                        
                        )

ORDINAL_CHOICES =(
                  ('1',"First"),
                  ('2',"Second"),
                  ('3',"Third"),
                  ('4',"Fourth"),
                  ('-1',"Last"),
                  
                  )
   
WEEKS_COUNT = (
               ('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),
               ('5','5'),
               ('6','6'),
               ('7','7'),
               ('8','8'),
               ('9','9'),
               ('10','10'),
               ('11','11'),
               ('12','12'),
               
               )

WEEKLY_COUNT = (
               ('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),
               ('5','5'),
               ('6','6'),
               )


MONTHLY_COUNT = (
               ('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),

               )
