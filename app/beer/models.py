from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=256)
    brewery = models.ForeignKey("brewery.Brewery", on_delete=models.CASCADE)
