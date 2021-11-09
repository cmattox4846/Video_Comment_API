from django.db import models

# Create your models here.
class Comments(models.Model):
    video_ID = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    comment_reply= models.CharField(max_length=200)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

