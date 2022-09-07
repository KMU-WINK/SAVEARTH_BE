from  .models import Trash
from rest_framework import serializers

class TrashSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Trash
        fields = ['id', 'user_id', 'trash_x', 'trash_y']