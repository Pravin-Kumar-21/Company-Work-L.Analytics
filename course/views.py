import json
import os
from django.conf import settings
from django.shortcuts import render


def course_list(request, *args, **kwargs):
    base_dir = settings.BASE_DIR
    file_path = os.path.join(base_dir, "api", "get_all_courses_API_response.json")
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            courses = data.get("courses", [])
    except (FileNotFoundError, json.JSONDecodeError):
        courses = []

    return render(
        request,
        "course-list/course-list.html",
        {"courses": courses},
    )


def course_detail_list(request, *args, **kwargs):

    course_id = kwargs.get("course_id")
    base_dir = settings.BASE_DIR
    file_path = os.path.join(base_dir, "api", "get_course_detail_API_response.json")
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if str(data.get("course_id")) == str(course_id):
                videos = data.get("videos", [])
            else:
                print(f"Course ID {course_id} not found in JSON")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        videos = []
    return render(request, "course-detail/course_details.html", {"videos": videos})
