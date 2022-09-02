from django.db import models
from users.models import User

class Trashcan(models.Model):
    address = models.CharField(max_length=64, primary_key=True)
    trashcan_x = models.FloatField()
    trashcan_y = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)