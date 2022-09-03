from .models import Trashcan
from rest_framework import serializers

class TrashcanSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    class Meta:
        model = Trashcan
        fields = ['address', 'trashcan_x', 'trashcan_y', 'user_id']
    