from django.urls import path, include
from . import views


urlpatterns = [
    path('blog-list/', views.BlogCategoryAPIView.as_view(), name='blog-cat-api'),
    path('post-list/', views.BlogPostListAPIView.as_view(), name='blog-post-api'),
    path('post-create/', views.BlogPostCreateAPIView.as_view(), name='blog-post-create-api'),

    # For comments
    path('comment-create/', views.CommentCreateAPI.as_view(), name='comment-create'),
    path('comment-list/', views.CommentListAPI.as_view(), name='comment-list'),
]