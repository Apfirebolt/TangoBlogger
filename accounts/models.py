from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from TangoBlogger import settings


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_pics', default='1.png')
    bio = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('accounts:dashboard')