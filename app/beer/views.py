from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import models


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


class BeerListView(ListView):
    model = models.Beer


class BeerUpdateView(UpdateView):
    model = models.Beer
    fields = ["name"]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy("beer:beer_detail", kwargs={"pk": self.kwargs["pk"]})
