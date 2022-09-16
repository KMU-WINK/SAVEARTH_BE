from .models import Trashcan
from rest_framework import serializers

class TrashcanSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.nickname")
    # post 불가능 / 읽어올 수만 있는 필드를 user_id에 지정해줌
    # -> post할 때 user_id필드를 써주지 않음
    # -> user_id는 user 모델의 id를 FK로 가져왔지만 json데이터로 변환할 땐 id대신 nickname으로 보이게 변환
    class Meta:
        model = Trashcan
        fields = ['id', 'user_id', 'trashcan_x', 'trashcan_y']
    # model에서는 필드 이름으로 user로 쓰이나 json으로 보일 땐 user_id라는 이름으로 보이게 함