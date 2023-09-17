from rest_framework import serializers
from .models import *
from django.utils.encoding import force_str, force_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator


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

class VerifyEmailSerializer(serializers.Serializer):
    token = serializers.CharField()
    user_id = serializers.CharField()

    def validate(self, attrs):
        try:
            token = attrs.get('token')
            user_id = attrs.get('user_id')
            uid = smart_str(urlsafe_base64_decode(user_id))
            user = AuthUser.objects.get(id=uid)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise ValidationError({'message': 'Invalid token or expired'})

            user.is_email_verified = True
            user.save()
            return attrs

        except (TypeError, ValueError, DjangoUnicodeDecodeError) as e:
            raise ValidationError({'message': 'Invalid token or expired'})
