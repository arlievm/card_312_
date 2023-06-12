from django.shortcuts import render

from rest_framework import generics

from .models import Discounts
from .serializers import DiscountsSerializer


class DiscountsCreateListView(generics.ListCreateAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()
    
class DiscountsView(generics.DestroyAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()