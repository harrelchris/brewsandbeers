from django.contrib import admin

from . import models

admin.site.register(models.Beer)
admin.site.register(models.BeerImage)
admin.site.register(models.BeerReview)
admin.site.register(models.Favorite)
