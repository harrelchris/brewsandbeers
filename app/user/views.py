from django.apps import apps
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

BeerReview = apps.get_model("beer", "BeerReview")


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("user:login")
    template_name = "user/register.html"


class LoginView(auth_views.LoginView):
    template_name = "user/login.html"


class LogoutView(auth_views.LogoutView):
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


class PasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy("user:password_change_done")
    template_name = "user/password_change_form.html"


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "user/password_change_done.html"


class ProfileView(TemplateView):
    template_name = "user/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer_review_list"] = BeerReview.objects.filter(user=self.request.user)
        return context
