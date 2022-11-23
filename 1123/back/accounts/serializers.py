from rest_framework import serializers
from django.contrib.auth import get_user_model
# from .models import User



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # image_url = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'like_movies', 'followings', 'followers', 'image')
        read_only_fileds = ('followings', 'followers', 'like_movies',)

class ProfilePictureSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(source='defaultprofilepic')

    class Meta:
        model = User
        fields = ('id', 'image', 'username',)
