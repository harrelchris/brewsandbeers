from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=256)
