from django.contrib import admin
from citysom.event.models import Place, Event,\
EventPublic, EventGenre, Category, PerformanceDetails, Days, UserComments

    
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('venue_name',)

class EventGenreAdmin(admin.ModelAdmin):
    list_display = ('genre_choices',)

class EventPublicAdmin(admin.ModelAdmin):
    list_display = ('choicelist',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('type',)

class EventAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('title','user','status')
    list_filter = ('user','status', 'category')
    search_fields = ( "title",)
 
class PerformanceDetailsAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('event','date_of_performance','showtimes_start','showtimes_end','ticket_price')
    search_fields = ( "event","place","ticket_price","showtimes_start","showtimes_end")
    list_filter = ('ticket_price',)
    
class DaysAdmin(admin.ModelAdmin):
    list_display = ('week_day',)

class UserCommentsAdmin(admin.ModelAdmin):
    list_display = ('event','ratings','status')
    
admin.site.register(Place, PlaceAdmin)   
admin.site.register(EventPublic, EventPublicAdmin)
admin.site.register(EventGenre, EventGenreAdmin)
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Event, EventAdmin)
admin.site.register(PerformanceDetails, PerformanceDetailsAdmin)
admin.site.register(Days, DaysAdmin)
admin.site.register(UserComments, UserCommentsAdmin)