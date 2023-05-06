from django.urls import path

from . import views

app_name = "beer"

urlpatterns = [
    path("", views.BeerListView.as_view(), name="beer_list"),
    path("create/", views.BeerCreateView.as_view(), name="beer_create"),
    path("<str:pk>/", views.BeerDetailView.as_view(), name="beer_detail"),
    path("update/<str:pk>/", views.BeerUpdateView.as_view(), name="beer_update"),
    path("delete/<str:pk>/", views.BeerDeleteView.as_view(), name="beer_delete"),
    path("<str:pk>/review/create/", views.ReviewCreateView.as_view(), name="review_create"),
    path("<str:pk>/image/create/", views.ImageCreateView.as_view(), name="image_create"),
]
