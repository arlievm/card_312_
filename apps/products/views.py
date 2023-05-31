from django.shortcuts import render
from rest_framework import generics

from .models import Products, Playbill
from .serializers import ProductsSerializer, PlaybillSerializer

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