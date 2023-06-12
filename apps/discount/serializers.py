from rest_framework import serializers as s

from .models import Discounts

class Discounts(serializers.Serializer):
    
    class Meta:
        model = Discounts
        fields = 'iamge','description','name'