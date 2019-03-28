from rest_framework import serializers
from blog.models import BlogPost, BlogCategory, Comment


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'blog_image']


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['title', 'owner', 'category']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = ('id', 'related_post', 'comment_by', 'comment_text', 'in_reply', 'commented_at')
        read_only_fields = ('id', 'commented_at')

