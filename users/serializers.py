from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('nickname', 'birth_year', 'birth_month', 'birth_day', 'gender')