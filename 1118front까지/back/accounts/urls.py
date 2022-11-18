from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    # user
    path('users/', views.users),
    # 회원가입 (vue에서 가능하면 필요없을지도)
    path('signup/', views.signup),

    # jwt
    path('api-token-auth/', obtain_jwt_token),

    # 내 프로필
    path('myprofile/', views.my_profile),

    # 팔로우 (내가 특정 user를)
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),

    # 특정 user의 정보
    path('info/', views.users_info),
    # 특정 user의 프로필
    path('<username>/', views.profile),
]
