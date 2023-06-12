from django.shortcuts import render
from rest_framework import generics

from apps.homes.models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreateListView(generics.ListCreateAPIView):
    serializer = FeedbackSerializer
    queryset = Feedback.objects.all()
    
class FeedbackDeteleview(generics.DeployAPIView):
    serializer = FeedbackSerializer
    queryset = Feedback.objects.all()
    