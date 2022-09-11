from .models import Trashcan
from rest_framework import serializers

class TrashcanSerializer(serializers.ModelSerializer):
    # 서버에서 자동으로 작성자 넣어줌
    user_id = serializers.ReadOnlyField(source="user.nickname")
    # csrftoken 사용시 위 코드 풀고 아래 두 코드 주석처리하고 fields의 user_name 삭제
    # user_id = serializers.CharField()
    # user_name = serializers.ReadOnlyField(source="user.nickname")
    class Meta:
        model = Trashcan
        fields = ['id', 'user_id', 'trashcan_x', 'trashcan_y']
    