from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name')
    # fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('first_name', 'last_name',)}),)
    
    
    
admin.site.register(CustomUser, CustomUserAdmin)