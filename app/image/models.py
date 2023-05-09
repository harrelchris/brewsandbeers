from django.db import models

from beer.models import Beer
from brewery.models import Brewery
from core.models import BaseModel
from location.models import Location

TYPES = [
    ("beer", "beer"),
    ("brewery", "brewery"),
    ("location", "location"),
]


class Image(BaseModel):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=256, choices=TYPES)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.type} - {self.image.url}"
