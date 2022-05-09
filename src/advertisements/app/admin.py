from advertisements.app import models
from django.contrib import admin

admin.site.register((models.Category, models.Offer))
