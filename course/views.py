from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
import requests
from django.contrib import messages
import json
from django.contrib.messages.views import SuccessMessageMixin
from . import mixins
import json
import os
import re


class LoginView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("course:course_list")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("course:course_list")


def log_out(request):
    logout(request)
    return redirect(reverse("home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("course:course_list")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


@login_required
def enroll_course(request, course_id):

    file_path = os.path.join(
        settings.BASE_DIR, "api", "get_all_courses_API_response.json"
    )
    with open(file_path, "r") as file:
        courses_data = json.load(file)
    course_data = None
    for course in courses_data["courses"]:
        if course["course_id"] == course_id:
            course_data = course
            break

    if not course_data:
        return render(request, "error.html", {"message": "Course not found."})
    enrolled_course, created = models.EnrolledCourse.objects.get_or_create(
        course_id=course_data["course_id"],
        defaults={
            "course_name": course_data["course_name"],
            "course_subject": course_data["course_subject"],
        },
    )
    user = request.user
    if isinstance(user, models.EnrolledCourse):
        enrolled_course.user_enrolled.add(user)
    return redirect("course:course_detail", course_id=course_id)


def save_note(request, course_id, video_id):
    course_id = course_id
    print(course_id)
    video_id = course_id

    if request.method == "POST":
        note_content = request.POST.get("note")

        if note_content:

            note, created = models.CourseNote.objects.get_or_create(
                member=request.user,
                video_id=video_id,
                course_id=course_id,
                defaults={"note": note_content},  # Default value if creating new
            )
            if not created:
                note.note += f"\n{note_content}"
            note.save()
            return redirect("course:course_detail", course_id=course_id)

    return render(
        request,
        "course-detail/course_details.html",
        {
            "video_id": video_id,
            "course_id": course_id,
        },
    )


def course_list(request, *args, **kwargs):
    base_dir = settings.BASE_DIR
    file_path = os.path.join(base_dir, "api", "get_all_courses_API_response.json")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            facets = data.get("facets", {})
            courses = data.get("courses", [])
    except (FileNotFoundError, json.JSONDecodeError):
        courses = []
        facets = {}

    selected_language = request.GET.get("language", "")
    selected_duration = request.GET.get("duration", "")
    selected_subject = request.GET.get("subject", "")
    selected_topic = request.GET.get("topic", "")
    search_query = request.GET.get("search", "").lower()

    if selected_language:
        courses = [
            course
            for course in courses
            if course.get("course_language").lower() == selected_language.lower()
        ]
    if selected_duration:
        courses = [
            course
            for course in courses
            if course.get("course_duration").lower() == selected_duration.lower()
        ]
    if selected_subject:
        courses = [
            course
            for course in courses
            if course.get("course_subject").lower() == selected_subject.lower()
        ]
    if selected_topic:
        courses = [
            course
            for course in courses
            if course.get("course_topic").lower() == selected_topic.lower()
        ]
    if search_query:
        courses = [
            course
            for course in courses
            if search_query in course.get("course_name", "").lower()
        ]

    return render(
        request,
        "course-list/course-list.html",
        {"courses": courses, "facets": facets},
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


@login_required
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
