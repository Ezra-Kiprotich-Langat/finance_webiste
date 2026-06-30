from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'is_verified', 'password']
        read_only_fields = ['íd', 'is_verified']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user