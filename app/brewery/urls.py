from django.urls import path

from . import views

app_name = "brewery"


# TODO: rename to list, create, image_create, location_create, location_image_create, etc.,
urlpatterns = [
    path("", views.BreweryListView.as_view(), name="brewery_list"),
    path("create/", views.BreweryCreateView.as_view(), name="brewery_create"),
    path("<str:pk>/", views.BreweryDetailView.as_view(), name="brewery_detail"),
    path("<str:pk>/update/", views.BreweryUpdateView.as_view(), name="brewery_update"),
    path("<str:pk>/delete/", views.BreweryDeleteView.as_view(), name="brewery_delete"),
    path(
        "<str:pk>/image/create/",
        views.BreweryImageCreateView.as_view(),
        name="brewery_image_create",
    ),
    path(
        "<str:pk>/location/create/",
        views.BreweryLocationCreateView.as_view(),
        name="brewery_location_create",
    ),
    path(
        "<int:pk>/location/<int:location_pk>/",
        views.BreweryLocationDetailView.as_view(),
        name="brewery_location_detail",
    ),
    path(
        "<int:pk>/location/<int:location_pk>/image/create/",
        views.BreweryLocationImageCreateView.as_view(),
        name="brewery_location_image_create",
    ),
    path(
        "<int:pk>/location/<int:location_pk>/review/create/",
        views.BreweryLocationReviewCreateView.as_view(),
        name="brewery_location_review_create",
    ),
]
