from django.urls import path
from course import views


app_name = "course"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    # path("course/<int:course_id>/", views.course_detail, name="course_detail"),
]
