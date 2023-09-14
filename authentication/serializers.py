from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = AuthUser
        fields = ["email"]

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['email','username', 'previous_password_date', 'previous_password_1',
                   'previous_password_2', 'groups', 'user_permissions', 'first_name', 'last_name', 'is_staff', 'email_confirmed', 'phone_number', 'two_factor_enabled']