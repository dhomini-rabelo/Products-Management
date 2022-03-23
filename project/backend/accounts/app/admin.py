from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm
from .models import User
from django.contrib import admin

admin.site.empty_value_display = 'NULL'




@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
    ("My fields", {"fields": ("img",)}),
    )
    list_display = 'first_name', 'username'
    list_display_links = 'first_name', 'username'
