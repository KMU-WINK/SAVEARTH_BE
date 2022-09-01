from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

from django.contrib.auth import login, logout
from rest_framework import permissions
from rest_framework import views, status
from rest_framework.response import Response

from . import serializers

# 회원가입
class UserCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 로그인
class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
    
    def get(self, reqeust):
        return Response(None, status=status.HTTP_202_ACCEPTED)

# 로그아웃
class LogoutView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_202_ACCEPTED)
    
    def get(self, reqeust):
        return Response(None, status=status.HTTP_202_ACCEPTED)

