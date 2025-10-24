from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return f'PK={self.pk}: {self.title}'
