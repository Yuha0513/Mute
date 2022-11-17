from django.urls import path
# from . import views_tmdb
from . import views

app_name = 'movies'

urlpatterns = [
    # 영화 데이터 로드 
    # path('tmdb/', views_tmdb.tmdb_data),

    # 홈 페이지
    path('', views.home),

    # 배우
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),

    # 영화
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),

    # 리뷰
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('movies/<int:movie_pk>/reviews/', views.review_create),

    # 커뮤니티
    path('community_list_create/', views.community_list_create),
    path('detail/<int:community_pk>/', views.community_detail), 
    path('community/<int:community_pk>/', views.community_update_delete),

    # 코멘트
    path('comments/<int:community_pk>', views.comment_list),
    path('<int:community_pk>/comment/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_delete),

    # 좋아요
    path('<int:my_pk>/<movie_title>/like/', views.movie_like),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users),

]
