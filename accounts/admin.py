from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

class AccountAdmin(UserAdmin):
    
    # for password coulumn readonly
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    #create links for coulumns like email ,first name,last name
    list_display_links = ('email','first_name','last_name')
    #last login,date joined coulumns are only readonly
    readonly_fields = ('last_login', 'date_joined')
    # by using date joined display accounts in decending order
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state','country')

# Register your models here.
admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)


