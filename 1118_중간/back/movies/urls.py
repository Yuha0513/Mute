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

    # 리뷰 수정 전 ( 오류 : 영화별로 리뷰를 달려고 했는데, 각 영화에 모든 리뷰가 출력된다! )
    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    # path('movies/<int:movie_pk>/reviews/', views.review_create),

    # 리뷰 수정 후 
    path('<int:movie_pk>/review_list_create/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_update_delete),

    # 좋아요
    path('<int:my_pk>/<movie_title>/like/', views.likeornot),
    path('<int:my_pk>/like/', views.Ilike),
    path('<int:my_pk>/like/users/', views.likeusers),

]
