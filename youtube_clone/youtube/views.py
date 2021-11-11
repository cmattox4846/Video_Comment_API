from django.http.response import Http404
from .models import Comments, Reply
from .serializers import CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
import time


class CommentList(APIView):
    def get(self,request):
        time.sleep(1)
        Comment = Comments.objects.all()
        serializer = CommentSerializer(Comment, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetails(APIView):
    time.sleep(1)
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


class ReplyList(APIView):
    time.sleep(1.5)
    def get(self,request):
        
        Replys = Reply.objects.all()
        serializer = ReplySerializer(Replys, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReplyDetails(APIView):
    def get_object(self,pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404
   
    def get(self,request, pk ):
        Replys = self.get_object(pk)
        serializer = ReplySerializer(Replys)
        return Response(serializer.data)

    def put(self,request,pk):
        Replys = self.get_object(pk)
        serializer = ReplySerializer(Replys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        Replys = self.get_object(pk)
        Replys.delete()
        return Response(status=status.HTTP_200_OK)


    
    
class CommentLike(APIView):
    def get_object(self,pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        Comment= self.get_object(pk)
        serializer = CommentSerializer.increase_likes(Comment, Comment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
       
        # return Response(serializer,status=status.HTTP_200_OK)

class CommentDislike(APIView):
    def get_object(self,pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404

    def put(self,request,pk):
        Comment = self.get_object(pk)
        serializer = CommentSerializer.increase_dislikes(Comment, Comment)
        
        
       
        return Response(serializer,status=status.HTTP_200_OK)
       
