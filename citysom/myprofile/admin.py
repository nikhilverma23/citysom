from django.contrib import admin
from citysom.myprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name')
    
admin.site.register(UserProfile, UserProfileAdmin)