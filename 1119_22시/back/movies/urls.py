from django.urls import path
# from . import views_tmdb
from . import views

app_name = 'movies'

urlpatterns = [
    # 영화 데이터 로드 
    # path('tmdb/', views_tmdb.tmdb_data),

    # 홈 페이지
    path('', views.home),

    #장르
    path('genres/', views.genre_list),

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

    # 좋아요 _ 영화 선택
    path('<int:my_pk>/<movie_title>/like/', views.like_movies),
    # 좋아요 한 영화들의 장르를 추출해서 좋아하는 장르 기반 영화 추천
    path('yourmovie/', views.yourmovie, name='yourmovie'),

    # 좋아하는 장르 선택 -> like_genre 에 해당 장르 영화들 저장 -> vue 에서 해당 목록 내에서 lodash 랜덤
    path('<int:my_pk>/<genre_name>/like/', views.like_genre),
    #  -> 장르 기반으로 영화 (랜덤 random) 추천
    # path('yourgenre/', views.yourgenre, name='yourgenre'),

    # 선호하는 국가 언어 선택 -> like_lang 에 해달 언어 영화들 저장 -> vue 에서 해당 목록 내에서 lodash 랜덤
    path('<int:my_pk>/<movie_original_language>/like/', views.like_lang),
    # -> 일치하는 original_language 의 영화 (랜덤 random) 추천
    # path('yourlang/', views.yourlang, name='yourlang'),
]
