from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from m7.accounts.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "first_name", "last_name", "email", "password1", "password2",),
            },
        ),
    )