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
from django.forms.models import model_to_dict

# 홈페이지
@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

# 장르
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
  me = user.objects.get(username=request.user.username)
  likes = me.like_movies.all()
  serializer = MovieListSerializer(likes, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

# 3. 추천 ( 인기순 / 좋아하는 영화의 장르 기반 )
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
  user = get_user_model()
  movies = Movie.objects.all()  # 무비 모델에서 무비 정보들은 전부 가져옴 ( 쿼리 셋 )
  me = user.objects.get(username=request.user.username)
  like_movies_genre = {}
  likes = me.like_movies.all().values() # 좋아하는 영화 정보 받아오기
  # 좋아요한 영화 쿼리셋이 존재하지 않을 경우, 평점 높은 영화 10개 추천
  if not likes:
    popular_movies = Movie.objects.all().order_by('-vote_average')
    # 평점 9.1 짜리 먼저 뜸
    pops_num = 0
    pop_movies = []
    for pop_movie in popular_movies:
      # 쿼리셋 -> dict 변환 필요
      pop_movie_data = model_to_dict(pop_movie)
      # pop_movie_data는 하나씩이야
      needs = { 'id' : pop_movie_data['id'], 'title' : pop_movie_data['title'], 'poster_path': pop_movie_data['poster_path'], 'original_language':pop_movie_data['original_language'] }
      pop_movies.append(needs)
      # pop_movies = [ { 영화 1의 id, title...  }, { 영화 2의 ...  } ]
      pops_num += 1
      if pops_num == 10:
        break
    context = {
      'movies':pop_movies,
    }
    return Response(context)
  # OR

  # 좋아요한 영화 쿼리셋이 존재할 경우, 알고리즘 기반 추천
  else:
    for movie in likes:
      movie = get_object_or_404(Movie, pk=movie['id'])
      movie_g = movie.genres.values()
      for genre in movie_g: # 장르들 중에 장르를 뽑았는데
        try:
          like_movies_genre[genre['id']] += 1
        except:
          like_movies_genre[genre['id']] = 1
    you_like = []
    for movie in movies:
      movie_data = model_to_dict(movie)  
      if movie in likes:
        # you_like.append((movie_data, 0))  # 이미 본 영화 제외해야하니까 0 주기 
        # print(movie)
        pass
      else: # 모든 영화 중 안 본 영화들 대상으로
        whole_genres = movie.genres.all() # 무비에 장르스 없음
        cnt = 0
        for genre in whole_genres:
          if like_movies_genre.get(genre.pk, False):
            cnt += like_movies_genre.get(genre.pk)
        if cnt > 1:
          you_like.append((movie_data, cnt))

        # you_like.append((movie_data, 0))  # 이미 본 영화 제외해야하니까 0 기점으로 -1 줘버리기 (절대 안 뜨게)
        # if movie in you_like:
        #   # 뽑아내 제외시키기
        #   you_like.remove((movie_data, cnt))

    you_like.sort(key=lambda x: x[1], reverse=True) # 큰수부터 추천
    recommend_movies_num = 0
    context_movie = []
    for movie in you_like:
      needs = { 'id' : movie[0]['id'], 'title' : movie[0]['title'], 'poster_path': movie[0]['poster_path'], 'original_language':movie[0]['original_language'] }
      context_movie.append(needs)
      recommend_movies_num += 1
      if recommend_movies_num == 10: # 10개까지
        break
    context = {
      'movies':context_movie,
    }
    return Response(context)

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

# # 랜덤 추첨
# import random

# # 1. user model의 like_genre 기반 랜덤 추첨
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def yourgenre(request, my_pk):
#   me = get_object_or_404(get_user_model(), pk=my_pk)
#   likes = me.like_genre.all() # 리스트가 아니라 원소인가?
#   random_genre_movie = []
#   for movies in likes:
#     random_movie = random.sample(movies, 3) # 리스트에서 뽑아와야하는데?
#     random_genre_movie.append(random_movie)
#   return Response(random_genre_movie)

# # 2. user model의 like_lang 기반 랜덤 추첨
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def yourlang(request, my_pk):
#   me = get_object_or_404(get_user_model(), pk=my_pk)
#   likes = me.like_lang.all()
#   random_lang_movie = []
#   for movies in likes:
#     random_movie = random.sample(movies, 3)
#     random_lang_movie.append(random_movie)
#   return Response(random_lang_movie)

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