from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User

class RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True)
    conf_password=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password','conf_password')


    def validate(self,data):
        username=data.get('username')
        password=data.get('password')
        conf_password=data.get('conf_password')
        email=data.get('email')
        if len(username)<7:
            raise ValidationError({'message':'username 8 ta belgidan kam bolmasligi kerak '})
        elif User.objects.filter(username=username):
            raise ValidationError({'message':'username band'})
        elif len(password)<7:
            raise ValidationError({'message':'password 8 ta belgidan kam blmasligi kerak'})
        elif User.objects.filter(email=email).exists():
            raise ValidationError({'message':'email band'})
        elif password!=conf_password:
            raise ValidationError({'message':'parollar mos emas'})
        return data


    def create(self, validated_data):
        validated_data.pop('conf_password')
        user=User.objects.create_user(**validated_data)
        return user


