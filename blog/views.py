from django.shortcuts import render , redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User , Post
from . serializers import UserSerializer , PostSerializer

# Create your views here.

class UserView(APIView):
    def get(self, request):
        pass

    def post(self , request):
        pass


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializers = PostSerializer(posts , many=True).data
        return Response(serializers)

    def post(self , request):
        serializers = PostSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=201)
        return Response(serializers)