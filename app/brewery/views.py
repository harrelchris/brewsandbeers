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


class BreweryCreateView(LoginRequiredMixin, CreateView):
    model = models.Brewery
    fields = [
        "name",
        "founded",
    ]
    template_name_suffix = "_create"
    success_url = reverse_lazy("brewery:brewery_list")


class BreweryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Brewery
    template_name_suffix = "_delete"
    success_url = reverse_lazy("brewery:brewery_list")


class BreweryDetailView(DetailView):
    model = models.Brewery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beer_list"] = Beer.objects.filter(brewery=self.get_object())
        context["review_list"] = models.BreweryReview.objects.filter(brewery=self.get_object())
        return context


class BreweryListView(ListView):
    model = models.Brewery


class BreweryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Brewery
    fields = [
        "name",
        "founded",
    ]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.kwargs["pk"]})


class ReviewCreateView(CreateView):
    model = models.BreweryReview
    fields = ["rating"]
    template_name = "brewery/brewery_review_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.brewery = models.Brewery.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = models.Brewery.objects.get(pk=self.kwargs["pk"])
        return context
