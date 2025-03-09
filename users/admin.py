from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'manager']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'manager')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
