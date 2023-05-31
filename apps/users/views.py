import uuid
import datetime

from django.conf import settings
from django.db.models import Sum
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.hashers import check_password, make_password

from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import parser_classes
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import SendMailSerializer, SendMessageSerializer
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserCRUDSerializer, CustomTokenRefreshSerializer, SendMessageSerializer

from apps.utils.main import generateError, generateAuthInfo


class MVSDynamicPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'update':
            if request.user.is_authenticated:
                return True
            else:
                return False
        else:
            return True


class UserMVS(viewsets.ModelViewSet):
    queryset = User.objects.all();
    permission_classes = [MVSDynamicPermission]
    lookup_field = 'uniqueId'
    serializer_class = UserSerializer

    def create(self, request):
        secretAdminKey = request.data.get('secretAdminKey');
        if secretAdminKey == settings.SECRET_ADMIN_KEY:
            serializer = UserCRUDSerializer(data={'password': settings.DEFAULT_PASSWORD}, context={'request': request});
            serializer.is_valid(raise_exception=True);
            serializer.save();
            return Response(data=f"{settings.CLIENT_URL}/user/{serializer.data['uniqueId']}");
        return Response(status=status.HTTP_403_FORBIDDEN);

    def update(self, request, *args, **kwargs):
        user = request.user;
        data = request.data.dict();
        serializer = UserCRUDSerializer(user, data=data, context={'request': request});
        serializer.is_valid(raise_exception=True);
        serializer.save();
        return Response(serializer.data);


class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all();
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        uniqueId = request.data.get('uniqueId');
        password = request.data.get('password');
        try:
            user = User.objects.get(uniqueId=uniqueId)
        except User.DoesNotExist:
            return Response(**generateError('DOES_NOT_EXIST'));
        checkPassword = check_password(password, user.password);
        if not checkPassword:
            return Response(**generateError('WRONG_PASSWORD'));
        serializer = self.serializer_class(user, context={'request': request});
        return Response(data=generateAuthInfo(user, serializer.data));


class ResetPasswordMVS(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCRUDSerializer;
    lookup_field = 'resetPasswordUUID';

    def create(self, request, *args, **kwargs):
        uniqueId = request.data.get('uniqueId');
        try:
            user = User.objects.get(uniqueId=uniqueId);
        except User.DoesNotExist:
            return Response(**generateError('USER_NOT_FOUND'));
        serializer = self.serializer_class(user, context={'request': request});
        data = serializer.data;
        if not data['email']:
            return Response(**generateError('EMAIL_NOT_SET'));
        try:
            uuidStr = uuid.uuid4();
            milliseconds_since_epoch = datetime.datetime.now().timestamp() * 1000;
            user.resetPasswordUUID = uuidStr;
            user.resetPasswordDate = int(milliseconds_since_epoch) + 3600000;
            user.save();
            html_message = f'<a href="{settings.CLIENT_URL}/reset-password/{uuidStr}">Click me</a>';
            send_mail(
                'Reset password',
                'Click this button to reset password',
                settings.EMAIL_HOST_USER,
                [data['email']],
                fail_silently=False,
                html_message=html_message
            );
            return Response();
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR);

    def retrieve(self, request, *args, **kwargs):
        resetPasswordUUID = kwargs[self.lookup_field];
        try:
            user = User.objects.get(resetPasswordUUID=resetPasswordUUID);
        except User.DoesNotExist:
            return Response(**generateError('NOT_FOUND'));
        serializer = self.serializer_class(user, context={'request': request});
        milliseconds_since_epoch = datetime.datetime.now().timestamp() * 1000;
        if int(milliseconds_since_epoch) > serializer.data['resetPasswordDate']:
            return Response(**generateError('EXPIRED'));
        return Response(status=status.HTTP_200_OK);

    def update(self, request, *args, **kwargs):
        resetPasswordUUID = kwargs[self.lookup_field];
        password = request.data.get('password');
        try:
            user = User.objects.get(resetPasswordUUID=resetPasswordUUID);
        except User.DoesNotExist:
            return Response(**generateError('NOT_FOUND'));
        serializer = self.serializer_class(user, context={'request': request});
        milliseconds_since_epoch = datetime.datetime.now().timestamp() * 1000;
        if int(milliseconds_since_epoch) > serializer.data['resetPasswordDate']:
            return Response(**generateError('EXPIRED'));
        updateSerializer = self.serializer_class(user, data={'password': password, 'resetPasswordDate': None, 'resetPasswordUUID': None}, context={'request': request},partial=True);
        updateSerializer.is_valid(raise_exception=True);
        updateSerializer.save();
        serializer = UserSerializer(updateSerializer.instance, context={'request': request});
        return Response(data=generateAuthInfo(user, serializer.data), status=status.HTTP_200_OK);


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class SendMailAPIView(APIView):

    def post(self, request):

        serializers = SendMailSerializer(data=request.data)
        if serializers.is_valid():
            first_name = serializers.validated_data.get('first_name')
            last_name = serializers.validated_data.get('last_name')
            email = serializers.validated_data.get('email')
            message = serializers.validated_data.get('message')
            send_mail('',  from_email=None, message=f'{first_name} {last_name} {email} {message}', recipient_list=['suppor-temir@mail.ru'])
            return Response(serializers.errors, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SendMailUserApiView(APIView):

    def post(self, request):

        serializer = SendMessageSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            mobile = serializer.validated_data.get('mobile')
            email = serializer.validated_data.get('email')

            city = serializer.validated_data.get('city')
            street = serializer.validated_data.get('street')
            building_name = serializer.validated_data.get('building_name')
            unit = serializer.validated_data.get('unit')
            description = serializer.validated_data.get('description')
            message = serializer.validated_data.get('message')
            send_mail('', from_email=None, message=f' first name: {first_name}\n last name: {last_name}\n email: {email}\n message: {message}\n mobile: {mobile}\n city: {city}\n street: {street}\n building name:  {building_name}\n unit:  {unit}\n description: {description}\n',
                      recipient_list=['temircard@gmail.com'])
            return Response(serializer.errors, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)