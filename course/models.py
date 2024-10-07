from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Enrollment(models.Model):
    # user = models.ForeignKey(UserAdmin, on_delete=models.CASCADE)
    course_id = models.IntegerField()
    course_name = models.CharField(
        max_length=200
    )  # Can be linked to a Course model for better integrity
    course_description = models.TextField(null=True, blank=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} enrolled in {self.course_name}"
