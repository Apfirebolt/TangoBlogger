from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView


urlpatterns = [

    path('test/', views.test, name='test'),

    path('', TemplateView.as_view(template_name='blog/home_blog.html'), name='blog-home'),
    path('create/', views.CreateBlog.as_view(), name='create-blog'),
    path('update/<int:pk>/', views.UpdateBlog.as_view(), name='update-blog'),
    path('delete/<int:pk>/', views.DeleteBlog.as_view(), name='delete-blog'),
    path('detail/<slug:slug>/', views.DetailBlog.as_view(), name='detail-blog'),
    path('list/', views.ListBlog.as_view(), name='list-blog'),
    path('blog_post/create/<slug:blog>/', views.CreateBlogPost.as_view(), name='create-post'),
    path('blog_post/list/', views.ListBlogPost.as_view(), name='list-post'),
    path('blog_post/update/<int:pk>/', views.UpdateBlogPost.as_view(), name='update-post'),

    path('blog_post/delete/<slug:slug>/', views.DeleteBlogPost.as_view(), name='delete-post'),

    path('api/', include(('blog.api.urls', 'blog.api'), namespace='blog-api'))
]