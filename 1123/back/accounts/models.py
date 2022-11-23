from django.db import models
from django.contrib.auth.models import AbstractUser

# like => movie랑 genre
from movies.models import Movie, Genre

def upload_to(instance, filename):
    return '{filename}'.format(filename=filename)

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    
    like_movies = models.ManyToManyField(Movie, related_name='user_movies') # 좋아하는 영화들
    like_genre = models.ManyToManyField(Genre, related_name='user_genre') # 좋아하는 장르
    like_lang = models.ManyToManyField(Movie, related_name='user_lang') # 선호하는 국가 언어

    image = models.ImageField(upload_to='upload_to', blank=True, null=True, default = './defaultprofilepic.jpg')

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     pic = models.ImageField(upload_to='upload_to', blank=True, null=True)
# from PIL import images