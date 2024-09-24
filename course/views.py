import json
import os
from django.conf import settings
from django.shortcuts import render
import re


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


def generate_embed_urls(youtube_urls):
    embed_urls = []
    for url in youtube_urls:
        video_id_match = re.search(
            r"(v=|/vi?/|youtu\.be/|\/embed\/|\/shorts\/)([^&?\/]+)", url
        )
        if video_id_match:
            video_id = video_id_match.group(2)
            embed_url = f"https://www.youtube.com/embed/{video_id}"
            embed_urls.append(embed_url)
        else:
            embed_urls.append("Invalid YouTube URL")
    return embed_urls


def course_detail_list(request, *args, **kwargs):
    videos = []
    yt_urls = []
    embed_urls = []
    course_id = kwargs.get("course_id")
    base_dir = settings.BASE_DIR
    file_path = os.path.join(base_dir, "api", "get_course_detail_API_response.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if str(data.get("course_id")) == str(course_id):
                videos = data.get("videos", [])

                yt_urls = [
                    video.get("youtube_url")
                    for video in videos
                    if "youtube_url" in video
                ]
                embed_urls = generate_embed_urls(yt_urls)
            else:
                print(f"Course ID {course_id} not found in JSON")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}")
        videos = []
    return render(
        request,
        "course-detail/course_details.html",
        {
            "videos": videos,
            "course_id": course_id,
            "embed_urls": embed_urls,
        },
    )
