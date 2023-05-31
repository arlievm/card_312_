from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from .models import Category
from .serializers import CategorySerializer


# CATEGORY
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True). \
        select_related('parent'). \
        prefetch_related('children',
                         'children__children',
                         'children__children__children')
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.filter()

    serializer_class = CategorySerializer