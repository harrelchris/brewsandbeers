from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Image
from beer.models import Beer
from brewery.models import Brewery
from location.models import Location


class ImageCreate(LoginRequiredMixin, CreateView):
    model = Image
    template_name = "image/image_create.html"
    fields = [
        "image",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = self.kwargs["type"]
        if self.kwargs["type"] == "beer":
            context["beer"] = Beer.objects.get(pk=self.kwargs["pk"])
        elif self.kwargs["type"] == "brewery":
            context["brewery"] = Brewery.objects.get(pk=self.kwargs["pk"])
        elif self.kwargs["type"] == "location":
            context["location"] = Location.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        if self.kwargs["type"] == "beer":
            form.instance.beer = Beer.objects.get(pk=self.kwargs["pk"])
        elif self.kwargs["type"] == "brewery":
            form.instance.brewery = Brewery.objects.get(pk=self.kwargs["pk"])
        elif self.kwargs["type"] == "location":
            form.instance.location = Location.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        view = "brewery:brewery_list"
        if self.kwargs["type"] == "beer":
            view = "beer:beer_detail"
        elif self.kwargs["type"] == "brewery":
            view = "brewery:brewery_detail"
        elif self.kwargs["type"] == "location":
            view = "location:location_detail"
        return reverse_lazy(view, kwargs={"pk": self.kwargs["pk"]})
