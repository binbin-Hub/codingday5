from django.db import models

# Create your models here.

class Channel(models.Model):
    channelname = models.CharField(max_length = 30)
    creatorname = models.CharField(max_length = 20)
    preference = models.IntegerField()
    onlive = models.BooleanField()
    subscriber = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
