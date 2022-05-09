from django.contrib import admin

from advertisements.app import models

admin.site.register((models.Category, models.Offer))
