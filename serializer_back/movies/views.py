from django.shortcuts import render
from functools import partial
from django.shortcuts import render
from .models import Actor, Movie, Genre, Review, Community, Comment
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, ReviewCommentSerializer, CommunityListSerializer, CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movies import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
# 1. 리뷰 목록
@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# 2. 리뷰 상세
@api_view(['DELETE', 'PUT', 'GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance = review, data = request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# 3. 리뷰 생성
@api_view(["POST"],)
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# 4. 리뷰 수정 및 삭제
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if not request.user.reviews.filter(pk=review_pk).exists():
    return Response({'message': 'unauthorized!'})
  if request.method == 'PUT':
    serializer = ReviewListSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      pre_point = movie.vote_average * (movie.vote_count - 1)
      pre_count = movie.vote_count - 1
      point = pre_point+request.data.get('rank')
      count = movie.vote_count
      new_vote_average = round(point/count, 2)
      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)
  else:
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=review.movie_id)
    pre_point = movie.vote_average * (movie.vote_count)
    pre_count = movie.vote_count
    point = pre_point - review.rank
    count = movie.vote_count-1
    new_vote_average = round(point/count, 2)
    movie.vote_average = new_vote_average
    movie.vote_count = count
    movie.save()
    review.delete()
    return Response({ 'id': review_pk })

# 리뷰 댓글
# 1. 리뷰 댓글 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  serializer = ReviewCommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user, review=review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
# 2. 리뷰 댓글 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_list(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comments = review.reviewcomment_set.all()
  serializer = ReviewCommentSerializer(comments, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)
# 3. 리뷰 댓글 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_delete(request, review_pk, review_comment_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comment = review.reviewcomment_set.get(pk=review_comment_pk)
  if not request.user.review_comments.filter(pk=review_comment_pk).exists():
    return Response({'message': 'unauthorized!'})
  else:
    comment.delete()
    return Response({ 'id': review_comment_pk })

# 좋아요
# 1. like or not - checking
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False 
  else:
      me.like_movies.add(movie.pk)
      liking = True
  return Response(liking)
# 2. I like these movies
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  data = []
  movies = request.data
  for movie_pk in movies:
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  return Response(data)
# 3. Whom like this movie
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')
  # print(movies)
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)
    # print(serializer.data)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)
  return Response(users)

# 커뮤니티
# 1. 글 상세
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)
  serializer = CommunityListSerializer(community)
  return Response(serializer.data, status=status.HTTP_200_OK)
# 2. 목록 및 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_list_create(request):
  if request.method == 'GET':
    communities = Community.objects.all()
    serializer = CommunityListSerializer(communities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  else:
    serializer = CommunityListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
# 3. 수정 및 삭제
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_update_delete(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)
  if not request.user.communities.filter(pk=community_pk).exists():
    return Response({'message': 'unauthorized!'})
  if request.method == 'PUT':
      serializer = CommunityListSerializer(community, data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
          return Response(serializer.data)
  else:
      community.delete()
      return Response({ 'id': community_pk })

#  커뮤니티 게시글에 다는 코멘트
#  1. 댓글 목록
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comments = community.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# 2. 댓글 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, community=community)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# 3. 댓글 수정 및 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, community_pk, comment_pk):
  community = get_object_or_404(Community, pk=community_pk)
  comment = community.comment_set.get(pk=comment_pk)
  if not request.user.comments.filter(pk=comment_pk).exists():
    return Response({'message': 'unauthorized!'})
  else:
    comment.delete()
    return Response({ 'id': comment_pk })