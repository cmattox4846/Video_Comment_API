from django.db import models

# Create your models here.
class Comments(models.Model):
    video_ID = models.CharField(max_length=50)
    comment = models.CharField(max_length=200, null=True,blank=True)
    comment_reply= models.CharField(max_length=200,null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True)
    dislikes = models.IntegerField(null=True,blank=True)

