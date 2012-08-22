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
               
    ('open_hour_based','Open Hour Based'),
    ('performance_based','Performance Based'),
    
    
)

DAYS_OF_WEEK = (
               
    ('0','MONDAY'),
    ('1','TUESDAY'),
    ('2','WEDNESDAY'),
    ('3','THURSDAY'),
    ('4','FRIDAY'),
    ('5','SATURDAY'),
    ('6','SUNDAY'),
    
)

FREQUENCY_CHOICES = (
                        ('ONCE','Once'),
                        ('DAILY','Daily'),
                        ('WEEKLY','Weekly'),
                        ('MONTHLY','Monthly'),
                        
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

SET_POS_CHOICES = (
                   ('1','First'),
                   ('2','Second'),
                   ('3','Third'),
                   ('4','Fourth'),
                   ('-1','Last'),
                   )

DAYS_OF_WEEK_SHORT = (
                        ('MO','MONDAY'),
                        ('TU','TUESDAY'),
                        ('WE','WEDNESDAY'),
                        ('TH','THURSDAY'),
                        ('FR','FRIDAY'),
                        ('SA','SATURDAY'),
                        ('SU','SUNDAY'),
                                          
                      )