from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.template.loader import render_to_string
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
