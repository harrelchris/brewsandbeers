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

Brewery = apps.get_model("brewery", "Brewery")


class BeerCreateView(LoginRequiredMixin, CreateView):
    model = models.Beer
    fields = ["name"]
    template_name_suffix = "_create"
    success_url = reverse_lazy("beer:beer_list")


class BeerDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Beer
    template_name_suffix = "_delete"
    success_url = reverse_lazy("beer:beer_list")


class BeerDetailView(DetailView):
    model = models.Beer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = Brewery.objects.get(pk=self.get_object().brewery.pk)
        context["review_list"] = models.BeerReview.objects.filter(
            beer_id=self.kwargs["pk"],
        )
        context["image_list"] = models.BeerImage.objects.filter(
            beer_id=self.kwargs["pk"],
        )
        return context


class BeerListView(ListView):
    model = models.Beer


class BeerUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Beer
    fields = ["name"]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = models.BeerReview
    fields = [
        "rating",
        "bitter",
        "sweet",
        "sour",
        "carbonation",
        "head",
        "smell",
        "text",
    ]
    template_name = "beer/beer_review_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.beer = models.Beer.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer"] = models.Beer.objects.get(pk=self.kwargs["pk"])
        return context


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = models.BeerImage
    fields = ["image"]
    template_name = "beer/beer_image_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.beer = models.Beer.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer"] = models.Beer.objects.get(pk=self.kwargs["pk"])
        return context
