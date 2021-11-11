from rest_framework import serializers
from .models import Comments, Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'video_ID','comment','likes','dislikes']
        like = serializers.SerializerMethodField('increase_likes')
        dislikes = serializers.SerializerMethodField('increase_dislikes')

    def increase_likes(self, obj):
        obj.likes += 1
        obj.save()

    def increase_dislikes(self, obj):
        obj.dislikes += 1
        obj.save()

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['comment','comment_reply']
        