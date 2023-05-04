from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=256)


class BreweryReview(models.Model):
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )
