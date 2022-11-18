from django.shortcuts import render
from functools import partial
from django.shortcuts import render
from .models import Actor, Movie, Genre, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# 홈페이지
@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# 배우
# 1. 배우 목록
@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# 2. 배우 상세
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 영화
# 1. 영화 목록
@api_view(['GET'])
def movie_list(request):
    movies= get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# 2. 영화 상세
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

# 리뷰
# 1&2. 리뷰 목록 조회 및 생성 ( ReviewListSerializer) ( review_list_create )
@api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])

def review_list_create(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  else:
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(movie=movie, user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

# 3-1. 리뷰 수정 & 삭제
@api_view(['DELETE', 'PUT'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk) 
    
    if request.method == 'PUT':
        serializer = ReviewListSerializer(instance = review, data = request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 좋아요 표시
# 1. like or not - checking
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def likeornot(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False 
  else:
      me.like_movies.add(movie.pk)
      liking = True
  return Response(liking)

# 내가 좋아하는 영화들
# 2. I like these movies
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def Ilike(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  data = []
  movies = request.data
  for movie_pk in movies:
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  return Response(data)

# 이 영화를 좋아하는 사람들
# 3. Whom like this movie
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def likeusers(request, my_pk):
  users = []
  movies = request.data.get('movies')
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)
  return Response(users)
