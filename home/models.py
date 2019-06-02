from django.db import models

# Create your models here.

class video(models.Model):
    videoName=models.CharField(max_length=200)
    videoDesc=models.CharField(max_length=200)
    url=models.CharField(max_length=200)
    videoId=models.CharField(max_length=200)
    publishedAt=models.IntegerField()