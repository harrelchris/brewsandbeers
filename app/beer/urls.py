from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "beer"

urlpatterns = [
    path("", views.BeerListView.as_view(), name="beer_list"),
    path("create/", login_required(views.BeerCreateView.as_view()), name="beer_create"),
    path("<str:pk>/", views.BeerDetailView.as_view(), name="beer_detail"),
    path("update/<str:pk>/", login_required(views.BeerUpdateView.as_view()), name="beer_update"),
    path("delete/<str:pk>/", login_required(views.BeerDeleteView.as_view()), name="beer_delete"),
    path("<str:pk>/review/create/", login_required(views.ReviewCreateView.as_view()), name="review_create"),
]
