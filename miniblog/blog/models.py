from django.db import models
from django.core.files.storage import default_storage


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        default_storage.delete(self.image.name)
        super().delete(using=using, keep_parents=keep_parents)