from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        login_required(views.PasswordChangeView.as_view()),
        name="password_change",
    ),
    path(
        "password_change/done/",
        login_required(views.PasswordChangeDoneView.as_view()),
        name="password_change_done",
    ),
    path("password_reset", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("profile/", login_required(views.ProfileView.as_view()), name="profile"),
]
