
from django.db.models import fields
from django.http.response import Http404
from django.shortcuts import render
from .models import Comments, Video
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status


# Create your views here.
class CommentList(APIView):
    def get(self,request):
        Video = Comments.objects.all()
        serializer = CommentSerializer(Video, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetails(APIView):
    def get_object(self,pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404
   
    def get(self,request, pk ):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(Comment)
        return Response(serializer.data)

    def put(self,request,pk):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(Comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Comment = self.get_object(pk)
        Comment.delete()
        return Response(status=status.HTTP_200_OK)

    
    
class CommentLike(APIView):
    def get_object(self,pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        Comment= self.get_object(pk)
        serializer = CommentSerializer.increase_like(Comment, Comment)
        
        
       
        return Response(serializer,status=status.HTTP_200_OK)

class VideoDislike(APIView):
    def get_object(self,pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        Comment = self.get_object(pk)
        serializer = CommentSerializer.increase_dislike(Comment, Comment)
        
        
       
        return Response(serializer,status=status.HTTP_200_OK)
       
