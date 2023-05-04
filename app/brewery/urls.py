from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "brewery"

urlpatterns = [
    path("", views.BreweryListView.as_view(), name="brewery_list"),
    path("create/", login_required(views.BreweryCreateView.as_view()), name="brewery_create"),
    path("<str:pk>/", views.BreweryDetailView.as_view(), name="brewery_detail"),
    path("update/<str:pk>/", login_required(views.BreweryUpdateView.as_view()), name="brewery_update"),
    path("delete/<str:pk>/", login_required(views.BreweryDeleteView.as_view()), name="brewery_delete"),
    path("<str:pk>/review/create/", login_required(views.ReviewCreateView.as_view()), name="review_create"),
]
