from advertisements.app import models
from advertisements.app import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response


class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all().order_by('ordering')
    serializer_class = serializers.CategorySerializer


class CategoryDetail(mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = models.Category.objects.all().order_by('ordering')
    serializer_class = serializers.CategorySerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class OfferList(generics.ListCreateAPIView):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer

    def list(self, request):
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


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer
