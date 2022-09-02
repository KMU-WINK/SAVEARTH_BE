from dataclasses import field
from pyexpat import model
from .models import Board, Comment
from rest_framework import serializers

class BoardSerialier(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'location', 'board_img', 'content', 'liked']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = ['id', 'board', 'user', 'comment']