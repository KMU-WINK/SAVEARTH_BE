from django.db import models
from users.models import User

class Route(models.Model):
    id = models.AutoField(primary_key = True, null = False, blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField(null = True)
    time = models.CharField(max_length=16)
    datetime = models.DateTimeField()
    distance = models.IntegerField()
    image = models.ImageField(upload_to="")
