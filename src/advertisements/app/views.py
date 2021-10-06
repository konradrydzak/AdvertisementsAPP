from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = models.Category.objects.all().order_by('ordering')
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def category_detail(request, id):
    category = models.Category.objects.filter(id=id)
    if not category:
        content = {'message': 'Requested resource was not found'}
        return Response(status=status.HTTP_404_NOT_FOUND, data=content)
    elif request.method == 'PUT':
        serializer = serializers.CategorySerializer(category.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def offer_list(request):
    if request.method == 'GET':
        category_query_param = request.query_params.get('category')
        if category_query_param:
            offers = models.Offer.objects.filter(category_id=category_query_param)
            if not offers:
                content = {'message': 'Requested resource was not found'}
                return Response(status=status.HTTP_404_NOT_FOUND, data=content)
        else:
            offers = models.Offer.objects.all()
        serializer = serializers.OfferSerializer(offers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def offer_detail(request, id):
    offer = models.Offer.objects.filter(id=id)
    if not offer:
        content = {'message': 'Requested resource was not found'}
        return Response(status=status.HTTP_404_NOT_FOUND, data=content)
    if request.method == 'GET':
        serializer = serializers.OfferSerializer(offer, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.OfferSerializer(offer.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
