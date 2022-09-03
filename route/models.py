from django.db import models
from users.models import User

class Route(models.Model):
    id = models.CharField(max_length=64, primary_key= True)
    steps = models.IntegerField()
    time = models.TimeField()
    distance = models.IntegerField()
    img = models.CharField(max_length=128)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
