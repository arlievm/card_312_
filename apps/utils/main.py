from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def generateError(errorCode):
    return {
        'status': status.HTTP_400_BAD_REQUEST,
        'data': {
            'error': True,
            'code': errorCode
        }
    }

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def generateAuthInfo(user, data):
    return {
        **get_tokens_for_user(user),
        'profile': data
    }