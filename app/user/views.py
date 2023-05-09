from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from beer.models import BeerReview
from location.models import Review as LocationReview


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("user:login")
    template_name = "user/register.html"


class LoginView(auth_views.LoginView):
    template_name = "user/login.html"


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """No modification required as long as LOGOUT_REDIRECT_URL is set in settings"""


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = "user/password_reset_email.html"
    subject_template_name = "user/password_reset_subject.txt"
    success_url = reverse_lazy("user:password_reset_done")
    template_name = "user/password_reset_form.html"


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "user/password_reset_done.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("user:password_reset_complete")
    template_name = "user/password_reset_confirm.html"


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "user/password_reset_complete.html"


class PasswordChangeView(LoginRequiredMixin, auth_views.PasswordChangeView):
    success_url = reverse_lazy("user:password_change_done")
    template_name = "user/password_change_form.html"


class PasswordChangeDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
    template_name = "user/password_change_done.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer_reviews"] = BeerReview.objects.filter(user=self.request.user)
        context["location_reviews"] = LocationReview.objects.filter(
            user=self.request.user,
        )
        return context


class UserDetail(DetailView):
    model = User
    template_name = "user/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer_reviews"] = BeerReview.objects.filter(user_id=self.kwargs["pk"])
        context["location_reviews"] = LocationReview.objects.filter(
            user_id=self.kwargs["pk"],
        )
        return context
