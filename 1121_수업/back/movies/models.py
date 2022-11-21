from django.db import models
from django.conf import settings
from unittest.util import _MAX_LENGTH
# from django.core.validators import MaxValueValidator, MinValueValidator

# 장르
class Genre(models.Model):
    name = models.CharField(max_length=50)

# 배우
class Actor(models.Model):
    name = models.CharField(max_length=50)

# 영화
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    actors = models.ManyToManyField(Actor, related_name='movies')
    original_language = models.CharField(max_length=100)


# 영화에 대한 리뷰 ( 게시글 )
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews")
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews") # 외래키
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)