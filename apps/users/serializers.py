from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']
        # exclude = ['password', 'groups', 'user_permissions', 'resetPasswordUUID', 'resetPasswordDate']


class UserCRUDSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=400, required=False)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(**validated_data);
        if validated_data['password']:
            user.set_password(validated_data['password']);
        user.save()
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value);
            else:
                setattr(instance, field, value)
        instance.save();
        return instance;


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs);
        decoded_payload = token_backend.decode(data['access'], verify=True);
        user_id = decoded_payload['user_id'];
        user = User.objects.get(id=user_id);
        data.update({
            'profile':
            UserSerializer(user, context={'request': self.context['request']}).data
        });
        return data


class SendMailSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=55)
    last_name = serializers.CharField(max_length=55)
    email = serializers.EmailField(max_length=55)
    message = serializers.CharField()


class SendMessageSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=55)
    last_name = serializers.CharField(max_length=55)
    mobile = serializers.CharField(max_length=55)
    email = serializers.EmailField(max_length=55)
    city = serializers.CharField(max_length=55)
    street = serializers.CharField(max_length=55)
    building_name = serializers.CharField(max_length=55)
    unit = serializers.CharField(max_length=55)
    description = serializers.CharField()