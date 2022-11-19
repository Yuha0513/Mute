from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    # 모든 유저 조회
    path('users/', views.users),

    # 회원가입 (vue에서 가능하면 필요없을지도)
    path('signup/', views.signup),

    # jwt 토큰
    # path('api-token-auth/', obtain_jwt_token),

    # 내 프로필 조회
    path('myprofile/', views.my_profile),

    # 다른 user 프로필
    path('<username>/profile/', views.user_profile),

    # 팔로우
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),
]
