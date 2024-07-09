from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class UserOutputSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]

class UserLogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    