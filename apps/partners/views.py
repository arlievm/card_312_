from django.shortcuts import render
from rest_framework import generics

from .models import Partners
from .serializers import PartnersSerializer


class PartnersCreateListView(generics.ListCreateAPIView):
    serializer_class = PartnersSerializer
    queryset = Partners.objects.all()
    
    
class PartnersDeleteView(generics.DestroyAPIView):
    serializer_class = PartnersSerializer
    queryset = Partners.objects.all()