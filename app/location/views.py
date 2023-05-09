from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
)

from .models import Location, Review
from brewery.models import Brewery
from image.models import Image


class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    template_name = "location/location_create.html"
    fields = [
        "street",
        "city",
        "state",
        "type",
        "tours",
        "capacity",
        "distribution",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = Brewery.objects.get(pk=self.kwargs["brewery_pk"])
        return context

    def form_valid(self, form):
        form.instance.brewery = Brewery.objects.get(pk=self.kwargs["brewery_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("location:location_detail", kwargs={"pk": self.object.pk})


class LocationDetail(DetailView):
    model = Location
    template_name = "location/location_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = Brewery.objects.get(pk=self.object.brewery.pk)
        context["images"] = Image.objects.filter(location=self.get_object())
        context["reviews"] = Review.objects.filter(location=self.get_object())
        return context


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "location/review_create.html"
    fields = [
        "text",
        "rating",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = Location.objects.get(pk=self.kwargs["location_pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = Location.objects.get(pk=self.kwargs["location_pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("location:location_detail", kwargs={"pk": self.object.location.pk})
