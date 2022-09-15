from django.db import models
from users.models import User

class Trashcan(models.Model):
    id = models.AutoField(primary_key = True, null = False, blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trashcan_x = models.FloatField()
    trashcan_y = models.FloatField()