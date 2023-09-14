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
