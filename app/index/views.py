from itertools import chain
from django.shortcuts import render, reverse
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


def search(request):
    query_string = request.GET.get("search")
    if query_string:
        beers = Beer.objects.filter(name__icontains=query_string)
        breweries = Brewery.objects.filter(name__icontains=query_string)
        locations = Location.objects.filter(brewery__name__icontains=query_string)

        results = []
        for beer in beers:
            result = {
                "text": beer.name,
                "link": reverse("beer:beer_detail", kwargs={"pk": beer.pk}),
                "type": "beer"
            }
            results.append(result)
        for brewery in breweries:
            result = {
                "text": brewery.name,
                "link": reverse("brewery:brewery_detail", kwargs={"pk": brewery.pk}),
                "type": "brewery"
            }
            results.append(result)
        for location in locations:
            result = {
                "text": f"{location.brewery.name} {location.city}, {location.state}",
                "link": reverse("location:location_detail", kwargs={"pk": location.pk}),
                "type": "location"
            }
            results.append(result)
        context = {
            "results": results
        }
        return render(
            request=request,
            template_name="index/search.html",
            context=context,
        )

