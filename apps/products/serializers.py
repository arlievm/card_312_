from rest_framework import serializers as s

from .models import Products, Playbill, Afishaslider,Discountslider
from apps.partners.serializers import PartnersSerializer


class ProductsSerializer(s.ModelSerializer):
    partners = PartnersSerializer()

    class Meta:
        model = Products
        fields = ['partners', 'image', 'discounts', 'name', 'description', 'data', 'price', 'id','price_size']


class PlaybillSerializer(s.ModelSerializer):

    class Meta:
        model = Playbill
        fields = ['image', 'title', 'description', 'price', 'id']
    
    
class AfishasliderSerializer(s.ModelSerializer): 
    
    class Meta:
        model = Afishaslider
        fields = 'photo','description'
    
class DiscountsliderSerializer(s.ModelSerializer):
    class Meta:
        model = Discountslider
        fields = 'image','description','title'
    