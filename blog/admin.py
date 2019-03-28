from django.contrib import admin
from .models import BlogCategory, BlogPost, SharedBlog, Comment

admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(SharedBlog)
admin.site.register(Comment)



