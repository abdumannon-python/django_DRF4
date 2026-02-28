from django.contrib.auth import authenticate

from .serializers import RegisterSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
class RegiterView(APIView):
    def post(self,request):
        serializer=RegisterSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        response={
            'status':status.HTTP_200_OK,
            'message':'royxatdan otdiz',
            'user':user.username
        }
        return Response(response)
class LoginView(APIView):
    def post(self,request):
        username=self.request.data.get('username')
        password=self.request.data.get('password')

        user=authenticate(username=username,password=password)

        if not user:
            raise ValidationError({'message':'username yoki parol xato'})

        token,_=Token.objects.get_or_create(user=user)

        response={
            'status': status.HTTP_200_OK,
            'message': 'Siz login qildiz',
            'data': str(token.key)
        }
        return Response(response)

