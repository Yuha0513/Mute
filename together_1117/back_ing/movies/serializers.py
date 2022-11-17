from rest_framework import serializers
from .models import Movie, Actor, Review, ReviewComment, Community, Comment

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

# 리뷰 => 상세 조회, 수정, 삭제
class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

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
    review_set = ReviewSerializer(many=True, read_only=True)
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

# 리뷰 목록 => 전체 목록 조회, 생성
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
    fields = ('movie_title', 'userName', 'title','content', 'user',)
    read_only_fileds = ('user',)

# 리뷰글의 댓글
class ReviewCommentSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = ReviewComment
    fields = ('id', 'userName', 'user', 'content', 'review', 'rank', 'created_at', 'updated_at',)
    read_only_fields = ('user', 'review',)

# 커뮤니티
class CommunityListSerializer(serializers.ModelSerializer):

  # 유저 이름
  userName = serializers.SerializerMethodField()

  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Community
    fields = ('id', 'userName', 'user', 'title', 'content', 'created_at', 'updated_at',)
    read_only_fields = ('user',)

# 코멘트
class CommentSerializer(serializers.ModelSerializer):

  # 유저 이름
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Comment
    fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
    read_only_fields = ('user','community',)
