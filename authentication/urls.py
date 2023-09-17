from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
       path('get-user', GetUsers.as_view(), name=''),
    path('user-exist', UserExistView.as_view(), name=''),
    path('email-verify/<user_id>/<token>', VerifyEmailView.as_view(), name=''),


]
