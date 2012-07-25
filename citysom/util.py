from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
        ('choices', '----------'),
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
               
    ('monday','MONDAY'),
    ('tuesday','TUESDAY'),
    ('wednesday','WEDNESDAY'),
    ('thursday','THURSDAY'),
    ('friday','FRIDAY'),
    ('saturday','SATURDAY'),
    ('sunday','SUNDAY'),
    
)

FREQUENCY_CHOICES = (
                        ('once','Once'),
                        ('daily','Daily'),
                        ('weekly','Weekly'),
                        ('monthly','Monthly'),
                        
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
