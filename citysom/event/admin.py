from django.contrib import admin
from citysom.event.models import Place, Event,\
EventPublic, EventGenre, Category, PerformanceDetails, Days 

    

    
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('venue_name',)

class EventGenreAdmin(admin.ModelAdmin):
    list_display = ('genre_choices',)
 

class EventPublicAdmin(admin.ModelAdmin):
    list_display = ('choicelist',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','user','status')
    list_filter = ('user','status', 'category')
 
class PerformanceDetailsAdmin(admin.ModelAdmin):
    list_display = ('showtimes_start','showtimes_end','ticket_price')

class DaysAdmin(admin.ModelAdmin):
    list_display = ('week_day',)
    
    
admin.site.register(Place, PlaceAdmin)   
admin.site.register(EventPublic, EventPublicAdmin)
admin.site.register(EventGenre, EventGenreAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Event, EventAdmin)
admin.site.register(PerformanceDetails, PerformanceDetailsAdmin)
admin.site.register(Days, DaysAdmin)