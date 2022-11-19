from django.db import models
from django.contrib.auth.models import AbstractUser

# like => movie랑 genre
from movies.models import Movie, Genre

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    
    like_movies = models.ManyToManyField(Movie, related_name='like_user1')
    like_genre = models.ManyToManyField(Genre, related_name='like_user2')
