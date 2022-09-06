from statistics import mode
from django.db import models
from users.models import User

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=100)
    location = models.CharField(max_length=10)
    board_img = models.ImageField(null=True)
    content = models.TextField()
    liked = models.IntegerField(default=0)
    comment_cnt = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def comment_up(self):
        self.comment_cnt += 1

class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    board = models.ForeignKey(Board, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment