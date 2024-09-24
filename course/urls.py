from django.urls import path
from course import views


app_name = "course"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("<int:course_id>/", views.course_detail_list, name="course_detail"),
]
