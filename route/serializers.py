from  .models import Route
from rest_framework import serializers

class RouteSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Route
        fields = ['id', 'user_id', 'steps', 'time', 'datetime', 'distance']