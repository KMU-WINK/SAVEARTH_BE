from .models import Board, Comment, Profile
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

class ProfileSerialier(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.id')
    nickname = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Profile
        fields = ['user', 'nickname']