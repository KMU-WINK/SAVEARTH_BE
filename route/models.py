from django.db import models
from users.models import User

class Route(models.Model):
    id = models.AutoField(primary_key = True, null = False, blank = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    distance = models.IntegerField()
    image = models.ImageField(upload_to="")
