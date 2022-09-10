from  .models import Route
from rest_framework import serializers

class RouteSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source = 'user.nickname')
    user_id = serializers.CharField()
    user_name = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Route
        fields = ['id', 'user_id', 'steps', 'starttime', 'endtime', 'distance', 'user_name']