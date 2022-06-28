from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    #the forms to change and add user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['pjnumber', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {"fields": ('pjnumber', 'email', 'password')}),
        ('personal info', {'fields': ()}),
        ('permissions', {'fields': ('admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'pjnumber', 'fname', 'lname', 'designation', 'section', 'station', 'password', 'password_2')}
            ),
    )
    search_fields  = ['pjnumber']
    ordering = ['pjnumber']
    filter_horizontal = ()

admin.site.register(User, UserAdmin)