from .models import Trashcan
from rest_framework import serializers

class TrashcanSerializer(serializers.ModelSerializer):
    # 서버에서 자동으로 작성자 넣어줌
    user_id = serializers.ReadOnlyField(source="user.nickname")
    class Meta:
        model = Trashcan
        fields = ['id', 'user_id', 'trashcan_x', 'trashcan_y']
    