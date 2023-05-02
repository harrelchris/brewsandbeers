from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models


class BreweryCreateView(CreateView):
    model = models.Brewery
    fields = ["name"]
    template_name_suffix = "_create"
    success_url = reverse_lazy("brewery:brewery_list")


class BreweryDeleteView(DeleteView):
    model = models.Brewery
    template_name_suffix = "_delete"
    success_url = reverse_lazy("brewery:brewery_list")


class BreweryDetailView(DetailView):
    model = models.Brewery


class BreweryListView(ListView):
    model = models.Brewery


class BreweryUpdateView(UpdateView):
    model = models.Brewery
    fields = ["name"]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.kwargs["pk"]})
