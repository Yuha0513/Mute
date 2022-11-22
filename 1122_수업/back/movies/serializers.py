from rest_framework import serializers
from .models import Movie, Actor, Review, Genre

# 배우 목록
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__' 

# 영화 목록
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# 장르 목록
class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name','id') 

# 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)  # 유효성 검사 에러 방지

# 영화         
class MovieSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model=Actor
            fields = ('name',)
            
    actors = ActorSerializer(many=True, read_only=True)

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')

    review_set = ReviewSerializer(many=True, read_only=True)  # 역참조

    class Meta:
        model = Movie
        fields = '__all__'

# 배우
class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = MovieSerializer(many=True, read_only=True,)
    class Meta:
        model = Actor
        fields = '__all__'

# 리뷰 목록
class ReviewListSerializer(serializers.ModelSerializer):

    # 리뷰가 달린 영화의 이름
    movie_title = serializers.SerializerMethodField()

    def get_movie_title(self, obj):
        return obj.movie.title

    # 유저 이름
    userName = serializers.SerializerMethodField()

    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('movie_title', 'userName', 'title','content', 'user',)
        read_only_fields = ('movie', 'user',)  # 유효성 검사 에러 방지

# # Model에서 받아오는 ModelSerializer 말고, 그냥 Serializer 만들기
# class RecommendSerializer(serializers.Serializer):


#     class MovieSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Movie
#             fields = ('title',)
#     movie = MovieSerializer(read_only=True)
