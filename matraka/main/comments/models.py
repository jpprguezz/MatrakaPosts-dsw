from django.conf import settings
from django.db import models


class Comment(models.Model):
    alias = models.CharField(max_length=128)
    content = models.TextField()
    post = models.ForeignKey(
        'posts.Post',  
        related_name='comments',  
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments',
        on_delete=models.CASCADE

    )