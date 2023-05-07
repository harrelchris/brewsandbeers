import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel

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


class Brewery(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    founded = models.IntegerField(
        validators=[
            MinValueValidator(1829),  # Yuengling founded in 1829
            MaxValueValidator(datetime.date.today().year),
        ],
    )

    def __str__(self):
        return self.name


class BreweryImage(BaseModel):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/brewery/")

    def __str__(self):
        return f"{self.brewery.name} - {self.pk}"


class BreweryLocation(BaseModel):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    type = models.CharField(max_length=256, choices=BREWERY_TYPES)
    tours = models.BooleanField()
    capacity = models.CharField(max_length=256, choices=CAPACITIES)
    distribution = models.CharField(max_length=256, choices=DISTRIBUTIONS)

    def __str__(self):
        return f"{self.brewery.name} - {self.city}, {self.state} - {self.pk}"


class BreweryLocationImage(BaseModel):
    brewery_location = models.ForeignKey(BreweryLocation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/brewery_location/")

    def __str__(self):
        return f"{self.brewery_location.brewery.name} - {self.brewery_location.city} - {self.pk}"


class BreweryLocationReview(BaseModel):
    brewery_location = models.ForeignKey(BreweryLocation, on_delete=models.CASCADE)
    text = models.TextField(max_length=4096)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    def __str__(self):
        return f"{self.brewery_location.brewery.name} by {self.user.username}"
