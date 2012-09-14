from django.contrib import admin
from citysom.myprofile.models import UserProfile, Wishlist,\
History, Popularity


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name')
    
admin.site.register(UserProfile, UserProfileAdmin)

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('event','user')
    
admin.site.register(Wishlist, WishlistAdmin)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('event','user')
    
admin.site.register(History, HistoryAdmin)

class PopularityAdmin(admin.ModelAdmin):
    list_display = ('event','popularity')
    
admin.site.register(Popularity, PopularityAdmin)