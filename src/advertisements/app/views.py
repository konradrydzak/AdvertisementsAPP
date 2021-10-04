from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['GET'])
def category_list(request):
    categories = models.Category.objects.all().order_by('ordering')
    serializer = serializers.CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def offer_list(request):
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


@api_view(['GET'])
def offer_by_id(request, id):
    offer = models.Offer.objects.filter(id=id)
    if not offer:
        content = {'message': 'Requested resource was not found'}
        return Response(status=status.HTTP_404_NOT_FOUND, data=content)

    serializer = serializers.OfferSerializer(offer, many=True)
    return Response(serializer.data)
