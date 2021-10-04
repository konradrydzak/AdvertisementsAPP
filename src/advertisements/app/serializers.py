from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = ['id', 'title', 'price', 'category_id']
