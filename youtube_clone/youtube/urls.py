from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetails.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('reply/<int:pk>/', views.ReplyDetails.as_view()),
    path('comment/<int:pk>/like/', views.CommentLike.as_view()),
    path('comment/<int:pk>/dislike/', views.CommentDislike.as_view()),
]