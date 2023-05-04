from django.apps import apps
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


class BeerCreateView(CreateView):
    model = models.Beer
    fields = ["name"]
    template_name_suffix = "_create"
    success_url = reverse_lazy("beer:beer_list")


class BeerDeleteView(DeleteView):
    model = models.Beer
    template_name_suffix = "_delete"
    success_url = reverse_lazy("beer:beer_list")


class BeerDetailView(DetailView):
    model = models.Beer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brewery"] = Brewery.objects.get(pk=self.get_object().brewery.pk)
        context["review_list"] = models.BeerReview.objects.filter(beer_id=self.kwargs["pk"])
        return context


class BeerListView(ListView):
    model = models.Beer


class BeerUpdateView(UpdateView):
    model = models.Beer
    fields = ["name"]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})


class ReviewCreateView(CreateView):
    model = models.BeerReview
    fields = ["rating"]
    template_name_suffix = "_create"
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
