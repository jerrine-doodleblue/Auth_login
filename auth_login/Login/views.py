from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  rest_framework.serializers import Serializer
from  rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
# Create your views here.

class LoginAPI(APIView):
    def get(self, request):
        pass

class RegisterAPI(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                print(serializer.validated_data)
                User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'], email=serializer.validated_data['email'])
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)