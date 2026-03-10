from http.client import responses

from django.contrib.auth import authenticate

from .serializers import RegisterSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User

class SignUp(APIView):
    def post(self,request):
        serializers=RegisterSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)

        response={
            'status':status.HTTP_201_CREATED,
            'message':'Siz royxatdan otdiz',
            'data':serializers.data
        }

        return Response(response)

class Login(APIView):
    def post(self,request):
        username=self.request.data.get('username')
        password=self.request.data.get('password')

        user=authenticate(username=username,password=password)
        if not user:
            raise ValidationError({'message':'xato'})

        refresh_token=RefreshToken.for_user(user)

        response={
            'status':status.HTTP_200_OK,
            'message':'Siz muffaqiyatli otdiz',
            'refresh':str(refresh_token),
            'access':str(refresh_token.access_token)
        }
        return Response(response)

class Logout(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self,request):
        try:
            refresh_token = self.request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout qilindi'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'Token xato'}, status=status.HTTP_400_BAD_REQUEST)
