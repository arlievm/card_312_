from rest_framework import serializers as s

from .models import Partners


# class RecursiveSerializer(s.Serializer):
    
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer.data


class PartnersSerializer(s.ModelSerializer):
    # children = RecursiveSerializer(many=True)

    class Meta:
        model = Partners
        fields = ['logo', 'image', 'mail', 'name', 'address', 'org', 'inn', 'activity_type',
                'description', 'phone_one', 'phone_two', 'phone_three', 'phone_four',
                'whatsapp', 'youtube', 'telegram', 'instagram', 'facebook', 'day', 'data_time', 'id'
                ]