from django.db import models
from django.contrib.auth.models import AbstractUser

# like => movie랑 genre
from movies.models import Movie, Genre

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    
    like_movies = models.ManyToManyField(Movie, related_name='user_movies') # 좋아하는 영화들
    like_genre = models.ManyToManyField(Genre, related_name='user_genre') # 좋아하는 장르
    like_lang = models.ManyToManyField(Movie, related_name='user_lang') # 선호하는 국가 언어
