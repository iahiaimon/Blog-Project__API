from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from .models import User, Post
from .serializers import UserSerializer, PostSerializer

# Create your views here.


class UserView(APIView):
    def get(self, request):
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True).data
        return Response(serializer)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "User created successfully"}, status=201)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True).data
        return Response(serializers)

    def post(self, request):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers)
