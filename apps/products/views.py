from django.shortcuts import render
from rest_framework import generics

from .models import Products, Playbill, Discountslider, Afishaslider
from .serializers import ProductsSerializer, PlaybillSerializer, AfishasliderSerializer, DiscountsliderSerializer

#### Продукт
class ProductCreateListView(generics.ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    
    
class ProductDeleteView(generics.DestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

######   Афиша
class PlaybillCreateListView(generics.ListCreateAPIView):
    serializer_class = PlaybillSerializer
    queryset = Playbill.objects.all()
    
    
class PlaybillDeleteView(generics.DestroyAPIView):
    serializer_class = PlaybillSerializer
    queryset = Playbill.objects.all()
    
    
class DiscountsliderCreateListView(generics.ListCreateAPIView):
    serializer_class = DiscountsliderSerializer
    queryset = Discountslider.objects.all()
    

class DiscountsliderDeteleView(generics.DestroyAPIView):
    serializer_class = DiscountsliderSerializer
    queryset = Discountslider.objects.all()


class AfishasliderCreateListView(generics.ListCreateAPIView):
    serializer_class = AfishasliderSerializer
    queryset = Afishaslider.objects.all()
    
class AfishasliderDeteleView(generics.DestroyAPIView):
    serializer_class = AfishasliderSerializer
    queryset = Afishaslider.objects.all()