from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel
from brewery.models import Brewery

TYPES = [
    ("Ale", "Ale"),
    ("Lager", "Lager"),
    ("Hybrid", "Hybrid"),
]

# https://www.brewersassociation.org/edu/brewers-association-beer-style-guidelines
STYLES = [
    ("Altbier", "Altbier"),
    ("Amber Ale", "Amber Ale"),
    ("American IPA", "American IPA"),
    ("American Lager", "American Lager"),
    ("American Pale Ale", "American Pale Ale"),
    ("American Stout", "American Stout"),
    ("Baltic Porter", "Baltic Porter"),
    ("Barley Wine", "Barley Wine"),
    ("Belgian Blond Ale", "Belgian Blond Ale"),
    ("Bitter", "Bitter"),
    ("Bock", "Bock"),
    ("Brown Ale", "Brown Ale"),
    ("Cream Ale", "Cream Ale"),
    ("Doppelbock", "Doppelbock"),
    ("Dubbel", "Dubbel"),
    ("Dunkel", "Dunkel"),
    ("German Pils", "German Pils"),
    ("Gose", "Gose"),
    ("Helles", "Helles"),
    ("Irish Red Ale", "Irish Red Ale"),
    ("Irish Stout", "Irish Stout"),
    ("Lambic", "Lambic"),
    ("Mild Ale", "Mild Ale"),
    ("Pale Lager", "Pale Lager"),
    ("Pilsner", "Pilsner"),
    ("Porter", "Porter"),
    ("Other", "Other"),
    ("Saison", "Saison"),
    ("Schwarzbier", "Schwarzbier"),
    ("Scotch Ale", "Scotch Ale"),
    ("Steam Beer", "Steam Beer"),
    ("Stout", "Stout"),
    ("Tripel", "Tripel"),
    ("Vienna Lager", "Vienna Lager"),
    ("Weizenbock", "Weizenbock"),
    ("Witbier", "Witbier"),
]


class Beer(BaseModel):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
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
