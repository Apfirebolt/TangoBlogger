from django.db import models
from TangoBlogger import settings

class SavedGallery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_gallery = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user_gallery)


class Gallery(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gallery_name = models.ForeignKey(SavedGallery, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.owner) + ' - ' + str(self.gallery_name)


