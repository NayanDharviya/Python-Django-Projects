from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm,UserAdminCreationForm
# Register your models here.

User=get_user_model()

class UserAdmin(BaseUserAdmin):
    #the forms to add and change user instances
    form=UserAdminChangeForm
    add_form=UserAdminCreationForm

    #the fields to be used in displayeing the user model
    #these override the definations on the base UserAdmin
    #that reference specific fields on auth.User

    list_display=('email','admin')
    list_filter=('admin','staff','active')
    fieldsets=(
        (None,{'fields':('full_name','mobile','email','password',)}),
        ('Permissions',{'fields':('admin','staff','active')}),
    )

    #add_fieldsets get_fieldsets to use this attribute when creating a user
    #overrides get_fieldssets to use this attribute when creating a user

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('full_name','mobile','email','password1','password2',)
        }),
    )
    search_fields=('email','full_name','mobile')
    ordering=('email',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)

#remove group model from admin side we're not using it
admin.site.unregister(Group)