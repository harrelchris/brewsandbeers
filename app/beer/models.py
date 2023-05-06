from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from models import BaseModel

TYPES = [
    ("Ale", "Ale"),
    ("Lager", "Lager"),
    ("Hybrid", "Hybrid"),
]

# https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines
# TODO: consider using table and foreign key rather than choices
STYLES = [
    ("Other", "Other"),
]


class Beer(BaseModel):
    name = models.CharField(max_length=256)
    brewery = models.ForeignKey("brewery.Brewery", on_delete=models.CASCADE)
    type = models.CharField(max_length=256, choices=TYPES)
    style = models.CharField(max_length=256, choices=STYLES)
    description = models.TextField(max_length=4096, null=True, blank=True)
    color = models.CharField(max_length=256, null=True, blank=True)
    abv = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    ibu = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(120),
        ],
    )

    def __str__(self):
        return f"{self.name} - {self.brewery.name}"


class BeerImage(BaseModel):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/beer/")

    def __str__(self):
        return f"{self.beer.brewery.name} - {self.beer.name} - {self.pk}"


class BeerReview(BaseModel):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    text = models.TextField(max_length=4096)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    bitter = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    sweet = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    sour = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    carbonation = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    head = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )
    smell = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
    )

    def __str__(self):
        return f"{self.beer.brewery.name} - {self.beer.name} by {self.user.username}"
