from django.db import models
from users.models import User

class Trash(models.Model):
    address = models.CharField(max_length=64, primary_key=True)
    trash_x = models.FloatField()
    trash_y = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)