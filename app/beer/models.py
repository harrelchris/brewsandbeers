from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

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


class Beer(models.Model):
    name = models.CharField(max_length=256)
    brewery = models.ForeignKey("brewery.Brewery", on_delete=models.CASCADE)
    type = models.CharField(max_length=256, choices=TYPES)
    style = models.CharField(max_length=256, choices=STYLES)
    abv = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    ibu = models.FloatField(validators=[MaxValueValidator(120), MinValueValidator(0)])
    description = models.TextField(max_length=4096, null=True)
    color = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f"{self.name} - {self.brewery.name}"


class BeerReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    bitter = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    sweet = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    sour = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    carbonation = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    head = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    smell = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    text = models.TextField(max_length=4096)

    def __str__(self):
        return f"{self.beer.brewery.name} - {self.beer.name} by {self.user.username}"


class BeerImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/beer/")

    def __str__(self):
        return f"{self.beer.brewery.name} - {self.beer.name} - {self.pk}"
