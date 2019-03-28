from django.db import models
from TangoBlogger import settings
from django.urls import reverse
from .validators import validate_file_extension
from django.utils.text import slugify


class BlogCategory(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=200)

    slug = models.CharField(max_length=500, editable=False)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return str(self.owner) + ' - ' + str(self.title)


class BlogPost(models.Model):
    blog = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)

    body = models.TextField()
    blog_image = models.FileField(upload_to="blog_images/", validators=[validate_file_extension], blank=True)
    is_shared = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog:detail-blog', kwargs={'slug':slugify(self.title)})

    def __str__(self):
        return self.title


class SharedBlog(models.Model):
    blog = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    likes = models.IntegerField()
    rated_by = models.ManyToManyField(settings.AUTH_USER_MODEL)
    ratings = models.IntegerField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.blog)


class Comment(models.Model):
    related_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=200)
    in_reply = models.ForeignKey('self', blank=True, null=True, related_name='comment_thread', on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment_text) + ' - ' + str(self.comment_by)
