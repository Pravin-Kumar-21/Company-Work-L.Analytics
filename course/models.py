from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Members(AbstractUser):
    """Member Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    first_name = models.CharField(
        _("first name"), max_length=30, blank=True, default=""
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )
    bio = models.TextField(default="", blank=True)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})


# EnrolledCourse model
class EnrolledCourse(models.Model):
    course_name = models.CharField(blank=True, max_length=200)
    course_id = models.IntegerField(blank=True, null=True)
    course_subject = models.CharField(blank=True, null=True, max_length=100)

    # ManyToManyField doesn't need on_delete
    enrolled_users = models.ForeignKey(
        "Members", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.course_name


# CourseNote model
class CourseNote(models.Model):
    member = models.ForeignKey(
        Members,
        related_name="notes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    video_id = models.CharField(null=True, blank=True, max_length=200)
    course_id = models.CharField(blank=True, null=True, max_length=100)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
