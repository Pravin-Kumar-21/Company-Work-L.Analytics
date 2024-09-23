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
