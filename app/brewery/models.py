import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

BREWERY_TYPES = [
    ("Brewery Only", "Brewery Only"),
    ("Taproom", "Taproom"),
    ("Brewpub", "Brewpub"),
    ("Beer Garden", "Beer Garden"),
    ("Other", "Other"),
]

CAPACITIES = [
    ("< 10", "< 10"),
    ("10-25", "10-25"),
    ("25-50", "25-50"),
    ("50-100", "50-100"),
    ("> 100", "> 100"),
]

DISTRIBUTIONS = [
    ("Cans", "Cans"),
    ("Bottles", "Bottles"),
    ("Kegs", "Kegs"),
    ("Growlers", "Growlers"),
    ("Draft", "Draft"),
    ("Other", "Other"),
]


class Brewery(models.Model):
    name = models.CharField(max_length=256)
    founded = models.IntegerField(
        validators=[MaxValueValidator(datetime.date.today().year), MinValueValidator(1829)]  # Yuengling founded in 1829
    )


class BreweryReview(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )


class BreweryImage(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    path = models.CharField(max_length=256)


class BreweryLocation(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    type = models.CharField(max_length=256, choices=BREWERY_TYPES)
    tours = models.BooleanField()
    capacity = models.CharField(max_length=256, choices=CAPACITIES)
    distribution = models.CharField(max_length=256, choices=DISTRIBUTIONS)
