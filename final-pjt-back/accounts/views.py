from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserAccountSerializer

User = get_user_model()


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'https://localhost:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


@api_view(['GET', 'POST'])
def user_information(request):

    user = request.user

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        user.nickname = request.data['nickname']
        user.save()

    serializer = UserAccountSerializer(user)

    return Response(serializer.data)


@api_view(['GET'])
def information(request, username):

    user = get_object_or_404(User, username=username)
    serializer = UserAccountSerializer(user)

    return Response(serializer.data)


@api_view(['PUT'])
def change_password(request):

    user = get_object_or_404(User, username=request.data.get('username', ' '))
    password = request.data.get('password', ' ')

    if check_password(user.password, password):
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    try:
        user.set_password(password)
        user.save()

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = UserAccountSerializer(user)

    return Response(serializer.data)
