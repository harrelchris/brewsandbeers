from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models

Beer = apps.get_model("beer", "Beer")


class BreweryListView(ListView):
    model = models.Brewery
    template_name = "brewery/brewery_list.html"


class BreweryDetailView(DetailView):
    model = models.Brewery
    template_name = "brewery/brewery_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer_list"] = Beer.objects.filter(brewery=self.get_object())
        context["image_list"] = models.BreweryImage.objects.filter(brewery=self.get_object())
        context["location_list"] = models.BreweryLocation.objects.filter(brewery=self.get_object())
        return context


class BreweryCreateView(LoginRequiredMixin, CreateView):
    model = models.Brewery
    template_name = "brewery/brewery_create.html"
    fields = [
        "name",
        "founded",
    ]

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.object.pk})


class BreweryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Brewery
    template_name = "brewery/brewery_update.html"
    fields = [
        "name",
        "founded",
    ]

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.object.pk})


class BreweryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Brewery
    template_name = "brewery/brewery_delete.html"
    success_url = reverse_lazy("brewery:brewery_list")


class BreweryImageCreateView(LoginRequiredMixin, CreateView):
    model = models.BreweryImage
    template_name = "brewery/brewery_image_create.html"
    fields = [
        "image",
    ]

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.object.brewery.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.brewery = models.Brewery.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = models.Brewery.objects.get(pk=self.kwargs["pk"])
        return context


class BreweryLocationCreateView(LoginRequiredMixin, CreateView):
    model = models.BreweryLocation
    template_name = "brewery/brewery_location_create.html"
    fields = [
        "street",
        "city",
        "state",
        "type",
        "tours",
        "capacity",
        "distribution",
    ]

    def get_success_url(self):
        return reverse_lazy(
            "brewery:brewery_location_detail",
            kwargs={
                "pk": self.object.brewery.pk,
                "location_pk": self.object.pk,
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = models.Brewery.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.brewery = models.Brewery.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)


class BreweryLocationDetailView(DetailView):
    model = models.BreweryLocation
    template_name = "brewery/brewery_location_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = models.Brewery.objects.get(pk=self.object.brewery.pk)
        context["image_list"] = models.BreweryLocationImage.objects.filter(brewery_location=self.get_object())
        context["review_list"] = models.BreweryLocationReview.objects.filter(brewery_location=self.get_object())
        return context


class BreweryLocationImageCreateView(LoginRequiredMixin, CreateView):
    model = models.BreweryLocationImage
    template_name = "brewery/brewery_location_image_create.html"
    fields = [
        "image",
    ]

    def get_success_url(self):
        return reverse_lazy(
            "brewery:brewery_location_detail",
            kwargs={
                "pk": self.object.brewery_location.brewery.pk,
                "location_pk": self.object.brewery_location.pk,
            }
        )

    def form_valid(self, form):
        form.instance.brewery_location = models.BreweryLocation.objects.get(pk=self.kwargs["location_pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = models.Brewery.objects.get(pk=self.kwargs["pk"])
        context["brewery_location"] = models.BreweryLocation.objects.get(pk=self.kwargs["location_pk"])
        return context


class BreweryLocationReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.BreweryLocationReview
    template_name = "brewery/brewery_location_review_create.html"
    fields = [
        "rating",
        "text",
    ]

    def get_success_url(self):
        return reverse_lazy(
            "brewery:brewery_location_detail",
            kwargs={
                "pk": self.object.brewery_location.brewery.pk,
                "location_pk": self.object.brewery_location.pk,
            }
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.brewery_location = models.BreweryLocation.objects.get(pk=self.kwargs["location_pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = models.Brewery.objects.get(pk=self.kwargs["pk"])
        context["brewery_location"] = models.BreweryLocation.objects.get(pk=self.kwargs["location_pk"])
        return context
