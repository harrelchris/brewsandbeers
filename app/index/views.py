from itertools import chain
from django.views.generic import TemplateView

from beer.models import Beer, BeerImage, BeerReview
from brewery.models import Brewery, Image
from location.models import Location, LocationImage, LocationReview


class Index(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["beers"] = Beer.objects.all()[:10]
        context["breweries"] = Brewery.objects.all()[:10]
        context["locations"] = Location.objects.all()[:10]
        context["beer_reviews"] = BeerReview.objects.filter(rating__gt=4).order_by(
            "created_at",
        )[:10]
        context["location_reviews"] = LocationReview.objects.filter(
            rating__gt=4,
        ).order_by("created_at")[:10]
        beer_images = BeerImage.objects.all()[:5]
        brewery_images = Image.objects.all()[:5]
        location_images = LocationImage.objects.all()[:5]
        context["images"] = list(chain(beer_images, brewery_images, location_images))
        return context


class Search(TemplateView):
    pass
