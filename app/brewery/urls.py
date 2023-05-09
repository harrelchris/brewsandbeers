from django.urls import path

from . import views

app_name = "brewery"

urlpatterns = [
    path("", views.BreweryList.as_view(), name="brewery_list"),
    path("<int:pk>", views.BreweryDetail.as_view(), name="brewery_detail"),
    path("create/", views.BreweryCreate.as_view(), name="brewery_create"),
    path("create/image/<int:brewery_pk>", views.ImageCreate.as_view(), name="image_create"),
]
