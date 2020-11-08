from django.db import models
from django.utils import timezone
from utils.utils import get_file_upload_path
from apps.user.models import UserModel


class PostModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to=get_file_upload_path)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    # relations
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
