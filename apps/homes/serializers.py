from rest_framework import serializers as s

from .models import Feedback
from apps.homes.serializers import FeedbackSerializer

class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        filds = 'sms', 'phone'