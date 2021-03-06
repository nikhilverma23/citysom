from django.utils.translation import ugettext_lazy as _


GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female'))
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
#EVENT_TYPE = (
#               
#    ('play','PLAY'),
#    ('movie','MOVIE'),
#    ('lecture','LECTURE'),
#    ('concerts','CONCERTS'),
#    ('sports','SPORTS'),
#    ('exhibition','EXHIBITION'),
#    
#)

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
                        ('never','Never'),
                        ('daily','Daily'),
                        ('weekly','Weekly'),
                        ('monthly','Monthly'),
                        ('other','Other(be specific)'),
                        
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