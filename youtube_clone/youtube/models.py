from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Comments(models.Model):
    video_ID = models.CharField(max_length=50)
    comment = models.CharField(max_length=200, null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True)
    dislikes = models.IntegerField(null=True,blank=True)

class Reply(models.Model):
  comment_reply= models.CharField(max_length=200)
  comment = models.ForeignKey(Comments,on_delete=models.CASCADE)

