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
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 리뷰 댓글 ( 리뷰 글에 대한 댓글 )
class ReviewComment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review_comments")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  review = models.ForeignKey(Review, on_delete=models.CASCADE) # 외래키

# 커뮤니티 ( 게시판 )
class Community(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="communities")
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# 코멘트 ( 게시판 댓글 )
class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  community = models.ForeignKey(Community, on_delete=models.CASCADE) # 외래키