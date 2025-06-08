from rest_framework.serializers import ModelSerializer

from .models import User , Post

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        