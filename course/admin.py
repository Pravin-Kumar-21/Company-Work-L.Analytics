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


@admin.register(models.EnrolledCourse)
class EnrolledPanel(admin.ModelAdmin):
    list_display = (
        "course_name",
        "course_id",
        "course_subject",
    )


@admin.register(models.CourseNote)
class CourseNotePanel(admin.ModelAdmin):
    list_display = (
        "course_id",
        "note",
        "created_at",
        "updated_at",
    )
