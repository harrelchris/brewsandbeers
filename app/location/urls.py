from django.urls import path

from . import views

app_name = "location"

urlpatterns = [
    path("<int:pk>/", views.LocationDetail.as_view(), name="location_detail"),
    path("<int:pk>/create/", views.LocationCreate.as_view(), name="location_create"),
    path("<int:pk>/image/", views.ImageCreate.as_view(), name="image_create"),
    path("<int:pk>/review/", views.ReviewCreate.as_view(), name="review_create"),
]
