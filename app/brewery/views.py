from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
)

from .models import Brewery
from beer.models import Beer
from image.models import Image
from location.models import Location


class BreweryList(ListView):
    model = Brewery
    template_name = "brewery/brewery_list.html"


class BreweryDetail(DetailView):
    model = Brewery
    template_name = "brewery/brewery_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beers"] = Beer.objects.filter(brewery=self.get_object())
        context["images"] = Image.objects.filter(brewery=self.get_object())
        context["locations"] = Location.objects.filter(brewery=self.get_object())
        return context


class BreweryCreate(LoginRequiredMixin, CreateView):
    model = Brewery
    template_name = "brewery/brewery_create.html"
    fields = [
        "name",
        "founded",
    ]

    def get_success_url(self):
        return reverse_lazy("brewery:brewery_detail", kwargs={"pk": self.object.pk})
