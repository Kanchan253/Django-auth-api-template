from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    class Meta:
        db_table = 'auth'


class AuthUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=False, blank=False, unique=False)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    email_confirmed = models.BooleanField(default=False)
    phone_number = models.CharField(default=None, max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on')
    modified_on = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    enabled_disabled_on = models.DateTimeField(auto_now_add=True)
    previous_password_date = models.DateTimeField(auto_now_add=True)
    previous_password_1 = models.CharField(max_length=255, blank=True, null=True)
    previous_password_2 = models.CharField(max_length=255, blank=True, null=True)
    two_factor_enabled = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    class Meta:
        db_table = 'auth'
