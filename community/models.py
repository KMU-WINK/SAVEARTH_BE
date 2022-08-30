from email.policy import default
from django.db import models

# Create your models here.
class Board(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=100)
    location = models.CharField(max_length=10)
    board_img = models.ImageField(null=True)
    content = models.TextField(null=False)
    liked = models.IntegerField(default=0)

class Comment(models.Model):
    idx=models.AutoField(primary_key=True)
    board_idx = models.IntegerField(null=False)
    writer=models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)