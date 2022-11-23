from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProfilePictureSerializer
from .models import User
from rest_framework import status

# 모든 유저 조회
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# 회원가입
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')
    if password != passwordConfirmation:
        return Response({ 'error': 'password incorrect!'})
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data)

# 내 프로필 조회
# @api_view(['POST'])
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(request, username):
    # user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'), username=username)
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)



# 다른 유저의 프로필 조회
# @api_view(['POST'])
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request, username):
    # user = get_object_or_404(get_user_model(), pk=request.data.get('user_pk'), username=username)
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# 팔로우 기능
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, my_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
            me.followings.remove(person)
            following = False
        else:
            me.followings.add(person)
            following = True
        print(me.followings.filter(pk=person.pk))
        return Response(following)

# @api_view(['GET','POT'])
# @permission_classes([IsAuthenticated])
# def create(request):
#     user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
#     if request.method == 'POST':
#         serializer = UserSerializer(request.Post, request.FILES)
#     else:
#         serializer = UserSerializer(user)
#     return Response(serializer.data)

# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def update(request, pk):
#     user = user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
#     if request.method == 'POST':
#         serializer = UserSerializer(request.Post, request.FILES, instance=user)
#     else:
#         serializer = UserSerializer(user)
#     return Response(serializer.data) 

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def profilepic(request):
    serializer = ProfilePictureSerializer(data=request.data)
    user = get_object_or_404(get_user_model(), pk=request.user.id)

    if request.method == 'GET':
        serializer = UserSerializer(user) # 프사 없으면 user 정보 띄우게
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:  # PUT 수정
        if serializer.is_valid():
            try:
                picture = User.objects.get(id=request.data['id'])
                picture.image = request.data['image']
                picture.save()
                serializer = ProfilePictureSerializer(picture, data=request.data, partial=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            except:
                return Response({'프로필 사진이 설정되지 않았습니다'}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)