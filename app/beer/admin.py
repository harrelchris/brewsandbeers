from django.contrib import admin

from . import models

admin.site.register(models.Beer)
admin.site.register(models.Review)
