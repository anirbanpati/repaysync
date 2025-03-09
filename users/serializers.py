from rest_framework import serializers
from .models import CustomUser
import random
import string

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'manager']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'manager', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password:
            # Auto-generate a random password if not provided
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
