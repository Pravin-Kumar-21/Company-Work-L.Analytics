from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.Members)
class UserAdminPanel(UserAdmin):
    """User Admin Panel"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                )
            },
        ),
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
