from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token
from . import views
import os
from datetime import datetime
import base64
from rest_framework import urls

app_name = 'accounts'

urlpatterns = [
    # 모든 유저 조회
    path('users/', views.users),

    # 회원가입 (vue에서 가능하면 필요없을지도)
    # path('signup/', views.signup),

    # jwt 토큰
    # path('api-token-auth/', obtain_jwt_token),

    # 내 프로필 조회
    path('myprofile/<username>/', views.my_profile),

    # 다른 user 프로필
    path('profile/<username>/', views.user_profile),

    # 팔로우
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),

    # 프로필 이미지 (조회get,업로드post)
    path('profilepic/', views.profilepic),

    # path('api-auth/', include('rest_framework.urls'))

    # # 프로필 이미지
    # path('create/', views.create),

    # # 프로필 이미지
    # path('update/', views.update),

]
