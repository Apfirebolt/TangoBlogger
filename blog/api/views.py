from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from rest_framework import generics
from rest_framework import permissions
from . serializers import BlogPostSerializer, BlogCategorySerializer, CommentSerializer
from blog.models import BlogPost, BlogCategory, Comment


class APITweet(TemplateView):

    template_name = 'gallery/test_api.html'


class BlogPostListAPIView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BlogPost.objects.all()


class BlogPostCreateAPIView(generics.CreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BlogCategoryAPIView(generics.ListAPIView):
    serializer_class = BlogCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        context = super(BlogCategoryAPIView, self).dispatch(request, **kwargs)
        print('Dispatch method was called : ', context)
        return context

    def get_queryset(self):
        print('Something related to API master')
        return BlogCategory.objects.all()


class CommentCreateAPI(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentListAPI(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()



