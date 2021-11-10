from django.db import models

# Create your models here.
class Comment(models.Model):
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    video_id = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)