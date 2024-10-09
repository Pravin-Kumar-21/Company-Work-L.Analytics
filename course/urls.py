from django.urls import path
from course import views


app_name = "course"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("<int:course_id>/", views.course_detail_list, name="course_detail"),
    path(
        "<int:course_id>/<str:video_id>/save_note",
        views.save_note,
        name="save_note",
    ),
    path("enroll/<int:course_id>/", views.enroll_course, name="enroll_course"),
]
