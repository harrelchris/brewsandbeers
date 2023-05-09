from django.urls import path

from . import views

app_name = "location"

urlpatterns = [
    path("<str:pk>/", views.LocationDetail.as_view(), name="location_detail"),
    path("create/<int:brewery_pk>", views.LocationCreate.as_view(), name="location_create"),
    path("create/review/<int:location_pk>", views.ReviewCreate.as_view(), name="review_create"),
]
