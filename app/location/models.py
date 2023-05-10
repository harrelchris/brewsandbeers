from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from brewery.models import Brewery
from core.models import BaseModel

TYPES = [
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


class Location(BaseModel):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    type = models.CharField(max_length=256, choices=TYPES)
    tours = models.BooleanField()
    capacity = models.CharField(max_length=256, choices=CAPACITIES)
    distribution = models.CharField(max_length=256, choices=DISTRIBUTIONS)

    def __str__(self):
        return f"{self.brewery.name} - {self.city}, {self.state} - {self.pk}"


class LocationImage(BaseModel):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/location/")

    def __str__(self):
        return f"{self.location.brewery.name} - {self.location.city}"


class LocationReview(BaseModel):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    text = models.TextField(max_length=4096)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    def __str__(self):
        return f"{self.location.brewery.name} by {self.user.username}"
