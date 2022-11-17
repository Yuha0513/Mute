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

    # 리뷰 ( 영화별로 리뷰를 달려고 했는데, 각 영화에 모든 리뷰가 출력된다! )

    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    # path('movies/<int:movie_pk>/reviews/', views.review_create),

    # 리뷰 수정
    # review_list               # ====> 둘이 같이
    # review_create             # ====> review_list_create   

    # review_detail
    # review_update_delete

    path('<int:movie_pk>/review_list_create/', views.review_list_create),
    path('review_detail/<int:review_pk>/', views.review_detail),
    path('review/<int:review_pk>/', views.review_update_delete),

    # 리뷰의 코멘트
    path('review_comments/<int:review_pk>', views.review_comment_list),
    path('<int:review_pk>/review_comment/', views.create_review_comment),
    path('review_comment/<int:review_pk>/<int:review_comment_pk>/', views.review_comment_delete),

    # 커뮤니티
    path('community_list_create/', views.community_list_create),
    path('detail/<int:community_pk>/', views.community_detail), 
    path('community/<int:community_pk>/', views.community_update_delete),

    # 코멘트
    path('comments/<int:community_pk>', views.comment_list),
    path('<int:community_pk>/comment/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_delete),

    # 좋아요
    path('<int:my_pk>/<movie_title>/like/', views.likeornot),
    path('<int:my_pk>/like/', views.Ilike),
    path('<int:my_pk>/like/users/', views.likeusers),

]
