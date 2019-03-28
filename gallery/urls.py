from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home_gallery, name='home-gallery'),
    path('create/', views.create_gallery, name='create-gallery'),
    path('list/', views.GalleryView.as_view(), name='list-gallery'),
    path('detail/<int:pk>', views.GalleryDetail.as_view(), name='detail-gallery'),
    path('update/<int:pk>', views.update_gallery, name='update-gallery'),
    path('update-util/<int:pk>', views.update_gallery_util, name='update-gallery-util'),
]