from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http.response import HttpResponseRedirect


class LoggedOutOnlyView(UserPassesTestMixin):
    permission_denied_message = "Erorr 404 Page Does Not Exist"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("course:course_list")


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")
