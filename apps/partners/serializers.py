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
        fields = "__all__"