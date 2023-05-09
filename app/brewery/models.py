import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel


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
