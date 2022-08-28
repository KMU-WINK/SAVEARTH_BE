from django.db import models

class eUser(models.Model):
    id = models.CharField(max_length=20, primary_key=True)

class Trash(models.Model):
    address = models.CharField(max_length=64, primary_key=True)
    trash_x = models.FloatField()
    trash_y = models.FloatField()
    user_id = models.ForeignKey(eUser, on_delete=models.CASCADE)

class Trashcan(models.Model):
    address = models.CharField(max_length=64, primary_key=True)
    trashcan_x = models.FloatField()
    trashcan_y = models.FloatField()
    user_id = models.ForeignKey(eUser, on_delete=models.CASCADE)

class Path(models.Model):
    id = models.CharField(max_length=64, primary_key= True)
    steps = models.IntegerField()
    time = models.TimeField()
    distance = models.IntegerField()
    img = models.CharField(max_length=128)
    user_id = models.ForeignKey(eUser, on_delete=models.CASCADE)

# Create your models here.
