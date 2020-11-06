from django.shortcuts import render
from rest_framework import viewsets, permissions
from members.models import User
from members.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    seiralizer_class = UserSerializer