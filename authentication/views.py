from django.shortcuts import render
from rest_framework import generics, status
from .models import AuthUser
from .serializers import *
from rest_framework.response import Response
from utils.enum_entity_event import CustomEnumEvents
from utils.response import JsonData
# Create your views here.
class GetUsers(generics.GenericAPIView):
    serializer_class = GetUserSerializer

    def get(self, request):
        try :
            queryset = AuthUser.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return JsonData(result=serializer.data,message=CustomEnumEvents.LIST_ALL_ITEMS_SUCCESS.name,status_code=status.HTTP_200_OK,status=True)
        except :
            return JsonData(result='No data found',message=CustomEnumEvents. GET_ITEM_NOT_FOUND.name,status_code=status.HTTP_204_NO_CONTENT,status=False)
class UserExistView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get("email")
        user = AuthUser.objects.filter(email=email).first()

        if not user:
            return JsonData(result={"exist": False}, status_code=status.HTTP_200_OK, status=True, message=CustomEnumEvents.USER_LOGIN.name)
        else:
            return JsonData(result={"exist": True}, status_code=status.HTTP_200_OK, status=True, message=CustomEnumEvents.USER_LOGIN.name)
    
class VerifyEmailView(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def get(self, request, user_id, token):
        serializer = self.serializer_class(data={'user_id': user_id, 'token': token})
        if serializer.is_valid(raise_exception=True) :
            return JsonData(message=CustomEnumEvents.USER_EMAIL_VERIFICATION_SUCCESS.name,result={'email': 'Successfully verified'}, status_code=status.HTTP_200_OK,status=True)
        else :
            return JsonData(message=CustomEnumEvents.USER_EMAIL_VERIFICATION_FAILED.name,result={'token': 'Invalid token'}, status_code=status.HTTP_400_BAD_REQUEST,status=False)