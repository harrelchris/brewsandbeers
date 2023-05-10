from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from .models import Beer, BeerImage, BeerReview, Favorite
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
        if self.request.user.is_authenticated:
            context["favorite"] = Favorite.objects.filter(beer=self.object, user=self.request.user).exists()
        else:
            context["favorite"] = False
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


def favorite(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, beer_id=pk).exists()
        if is_favorite:
            Favorite.objects.filter(user=request.user, beer_id=pk).delete()
            return JsonResponse(data={"result": "removed"})
        else:
            beer = Beer.objects.get(pk=pk)
            fav = Favorite(beer=beer, user=request.user)
            fav.save()
            return JsonResponse(data={"result": "added"})
    return JsonResponse({"result": "no-op"})
