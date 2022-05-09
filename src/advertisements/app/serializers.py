from rest_framework import serializers

from advertisements.app import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'ordering']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Offer
        fields = ['id', 'title', 'price', 'category_id']
