from django.shortcuts import render
from functools import partial
from django.shortcuts import render
from .models import Actor, Movie, Genre, Review
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, GenreListSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import JsonResponse

# 홈페이지
@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# 르
@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
  else: # POST
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(movie=movie, user=request.user) # 유저 정보
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

# 내가 좋아하는 영화 선택 ( 좋아요! 버튼 ) -> user model에 like_movies
# 1. 특정 영화에 좋아요를 하는 함수
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movies(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      likemovies = False 
  else:
      me.like_movies.add(movie.pk) # 내가 좋아하는 영화 목록에 추가
      likemovies = True
  return Response(likemovies)

# 좋아요 한 영화들(like_movies)의 장르를 추출해서 좋아하는 장르 기반 영화 추천 def
# 2. 당신이 좋아할만한 영화 추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def yourmovie(request):
  user = get_user_model()
  movies = Movie.objects.all()
  me = user.objects.get(username=request.user.username)
  like_movies_genre = {}
  likes = me.like_movies.all() # 좋아하는 영화 정보 받아오기
  # 내가 좋아하는 영화 기반으로 선호 장르 추출
  for movie in likes:
    movie_genre = movie.genres.all()
    for genre in movie_genre:
      like_movies_genre[genre.pk] = like_movies_genre.get(genre.pk, 0) + 1
  you_like = []
  for movie in movies:
    if movie in likes:
      you_like.append((movie, 100))
    else:
      whole = movie.genres.all()
      cnt = 0
      for genre in whole:
        if like_movies_genre.get(genre.pk, False):
          cnt += like_movies_genre.get(genre.pk)
        if cnt:
          you_like.append((movie, cnt))
  you_like.sort(key=lambda x: x[1], reverse=True) # 큰수부터
  recommend_movies_num = 0
  context_movie = []
  for movie in you_like:
    context_movie.append(movie[0])
    recommend_movies_num += 1
    if recommend_movies_num == 10:
      break
  context = {
    'movies':context_movie,
  }
  return JsonResponse(context)
  # return Response(context)

# 좋아하는 장르를 선택하게 해서 영화 추천
# 1. 내가 좋아하는 장르 선택 ( 장르 선택 버튼 만들어서 (좋아요 버튼 처럼) -> 해당 장르 영화들의 목록을 넘겨줌 )
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_genre(request, my_pk, movie_genres):
  movie = get_object_or_404(Movie, genres=movie_genres)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_genre.filter(pk=movie.pk).exists():
      me.like_genre.remove(movie.pk)
      likegenre = False 
  else:
      me.like_genre.add(movie.pk) # 유저가 선호하는 장르의 영화들 목록 = like_genre
      likegenre = True
  return Response(likegenre)

# 선호 언어 기반
# 1. 선호 언어 선택
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_lang(request, my_pk, movie_original_language):
  movie = get_object_or_404(Movie, original_language=movie_original_language)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_lang.filter(pk=movie.pk).exists():
      me.like_lang.remove(movie.pk)
      likelang = False 
  else:
      me.like_lang.add(movie.pk) # 유저가 선호하는 언어의 영화들 목록 = like_lang
      likelang = True
  return Response(likelang)

# 랜덤 추첨
import random

# 1. user model의 like_genre 기반 랜덤 추첨
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def yourgenre(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  likes = me.like_genre.all() # 리스트가 아니라 원소인가?
  random_genre_movie = []
  for movies in likes:
    random_movie = random.sample(movies, 3) # 리스트에서 뽑아와야하는데?
    random_genre_movie.append(random_movie)
  return Response(random_genre_movie)

# 2. user model의 like_lang 기반 랜덤 추첨
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def yourlang(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  likes = me.like_lang.all()
  random_lang_movie = []
  for movies in likes:
    random_movie = random.sample(movies, 3)
    random_lang_movie.append(random_movie)
  return Response(random_lang_movie)

# # 2. user model의 like_genre 기반 랜덤 추첨
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def yourgenre(request):
#   user = get_user_model()
#   movies = Movie.objects.all()
#   me = user.objects.get(username=request.user.username)
#   like_genre_movies = {}
#   my_genre = user.like_genre.all() # 좋아하는 장르 정보 받아오기
#   # 내가 좋아하는 장르 기반으로 영화 랜덤 추첨
#   for genre in my_genre: # genre.pk 가 담겨있음
#     movie_genre = movie.genres.all()
#     for genre in movie_genre:
#       like_genre_movies[genre.pk] = like_genre_movies.get(genre.pk, 0) + 1
#   your_genre_movies = []
#   for movie in movies:
#     if movie[genre] in like_genre_movies:
#       your_genre_movies.append(movie)
#   context = {
#     'mygenremovies': your_genre_movies,
#   }
#   return JsonResponse(context)
#   # return Response(context)

# # 2. 선호 언어 기반 추천 영화
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def yourlang(request):
#   user = get_user_model()
#   movies = Movie.objects.all()
#   me = user.objects.get(username=request.user.username)
#   like_lang_movies = {}
#   my_lang = user.like_lang.all()
#   for lang in my_lang:
#     movie_original_language = movie.original_language.all()
#     for original_language in movie_original_language:
#       like_lang_movies[original_language.pk] = like_lang_movies.get(original_language.pk, 0) + 1
#   your_lang_movies = []
#   for movie in movies:
#     if movie[original_language] in like_lang_movies:
#       your_lang_movies.append(movie)
#   context = {
#     'mylangmovies': your_lang_movies,
#   }
#   return JsonResponse(context)
#   # return Response(context)