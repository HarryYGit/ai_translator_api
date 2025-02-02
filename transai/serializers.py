from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Serializer for User Registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password': {'write_only': True},  # Password won't be readable in the response
            'is_staff': {'default': False},
            'is_superuser': {'default': False},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            is_staff=validated_data.get('is_staff', False),  # Handle is_staff
            is_superuser=validated_data.get('is_superuser', False) 
        )
        user.set_password(validated_data['password'])  # Securely hash the password
        user.save()
        return user
    

# # Serializer for User Login
class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Must include both username and password.")
        
        data['user'] = user
        return data
