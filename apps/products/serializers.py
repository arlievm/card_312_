from rest_framework import serializers as s

from .models import Products, Playbill
from apps.partners.serializers import PartnersSerializer


class ProductsSerializer(s.ModelSerializer):
    partners = PartnersSerializer()

    class Meta:
        model = Products
        fields = ['partners', 'image', 'discounts', 'name', 'description', 'data', 'price', 'id']


class PlaybillSerializer(s.ModelSerializer):

    class Meta:
        model = Playbill
        fields = ['image', 'title', 'description', 'price', 'id']