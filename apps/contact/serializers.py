from rest_framework import serializers as s

from .models import Contact
from apps.contact.serializers import ContactSerializer

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        filds = 'name', 'phone', 'email' , 'email_e'