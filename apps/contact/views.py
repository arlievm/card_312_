
from django.shortcuts import render
from rest_framework import generics

from .models import Contants
from .serializers import ContantsSerializer



class ContantsCreateListView(generics.ListCreateAPIView):
    serializer_class = ContantsSerializer
    queryset = Contacts.objects.all()

class ContantsDeteleView(generics.DestroyAPIView):
    serializer_class = Contacts
    queryset = Contacts.objects.all()