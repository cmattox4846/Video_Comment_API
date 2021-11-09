
from django.db.models import fields
from django.http.response import Http404
from django.shortcuts import render
from .models import Video
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status


# Create your views here.
class VideoList(APIView):
    def get(self,request):
        Video = Video.objects.all()
        serializer = CommentSerializer(Video, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoDetails(APIView):
    def get_object(self,pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404
   
    def get(self,request, pk ):
        Video = self.get_object(pk)
        serializer = CommentSerializer(Video)
        return Response(serializer.data)

    def put(self,request,pk):
        Video = self.get_object(pk)
        serializer = CommentSerializer(Video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Video = self.get_object(pk)
        Video.delete()
        return Response(status=status.HTTP_200_OK)

    
    
class VideoLike(APIView):
    def get_object(self,pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        Video = self.get_object(pk)
        serializer = CommentSerializer.increase_like(Video, Video)
        
        
       
        return Response(serializer,status=status.HTTP_200_OK)

class VideoDislike(APIView):
    def get_object(self,pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        Video = self.get_object(pk)
        serializer = CommentSerializer.increase_dislike(Video, Video)
        
        
       
        return Response(serializer,status=status.HTTP_200_OK)
       
