from django.db import models
from users.models import User

class Trash(models.Model):
    id = models.AutoField(primary_key = True, null = False, blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trash_x = models.FloatField()
    trash_y = models.FloatField()