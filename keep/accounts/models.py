from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Genre
# 장르는 필요 없음 Genre

# Following & Like 기능 vue에서 구현가능?

# 여행 목적지는 DB에 저장 안 함

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movies = models.ManyToManyField(Movie, related_name='like_user1')
    like_genre = models.ManyToManyField(Genre, related_name='like_user2')
