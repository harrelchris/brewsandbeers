from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from .models import Beer, BeerImage, BeerReview
from brewery.models import Brewery


class BeerCreate(LoginRequiredMixin, CreateView):
    model = Beer
    template_name = "beer/beer_create.html"
    fields = [
        "name",
        "type",
        "style",
        "description",
        "color",
        "abv",
        "ibu",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = Brewery.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.brewery = Brewery.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.object.pk})


class BeerDetail(DetailView):
    model = Beer
    template_name = "beer/beer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = Brewery.objects.get(pk=self.object.brewery.pk)
        context["images"] = BeerImage.objects.filter(beer=self.object)
        context["reviews"] = BeerReview.objects.filter(beer=self.object)
        return context


class BeerList(ListView):
    model = Beer
    template_name = "beer/beer_list.html"


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = BeerReview
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
    template_name = "beer/review_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer"] = Beer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.beer = Beer.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})


class ImageCreate(LoginRequiredMixin, CreateView):
    model = BeerImage
    template_name = "beer/image_create.html"
    fields = [
        "image",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer"] = Beer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.beer = Beer.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})
