from django.contrib import admin

from . import models

admin.site.register(models.Brewery)
admin.site.register(models.BreweryImage)
admin.site.register(models.BreweryLocation)
admin.site.register(models.BreweryLocationImage)
admin.site.register(models.BreweryLocationReview)
