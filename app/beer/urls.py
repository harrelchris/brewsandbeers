from django.urls import path

from . import views

app_name = "beer"

urlpatterns = [
    path("", views.BeerList.as_view(), name="beer_list"),
    path("<int:pk>/", views.BeerDetail.as_view(), name="beer_detail"),
    path("<int:pk>/create/", views.BeerCreate.as_view(), name="beer_create"),
    path("<int:pk>/image/", views.ImageCreate.as_view(), name="image_create"),
    path("<int:pk>/review/", views.ReviewCreate.as_view(), name="review_create"),
    path("<int:pk>/favorite/", views.favorite, name="favorite"),
]
