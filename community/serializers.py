from .models import Board, Comment, Liked
from rest_framework import serializers

class BoardSerialier(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'location', 'board_img', 'content', 'like_cnt', 'comment_cnt']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'board', 'user', 'comment']

class LikedSerialier(serializers.ModelSerializer):
    class Meta:
        model = Liked
        fields = ['user', 'like_posts']