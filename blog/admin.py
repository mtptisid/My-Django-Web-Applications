from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Customize the user admin interface if needed

admin.site.register(CustomUser, CustomUserAdmin)

