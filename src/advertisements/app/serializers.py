from advertisements.app import models
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'ordering']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = ['id', 'title', 'price', 'category_id']
