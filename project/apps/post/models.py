from django.db import models
from django.utils import timezone
from utils.abstract import DateTimeAbstractModel
from utils.utils import get_file_upload_path
from apps.user.models import UserModel, VisitorModel


class PostModel(DateTimeAbstractModel):
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


class PostCommentModel(DateTimeAbstractModel):
    text = models.TextField()
    # relations
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(VisitorModel, on_delete=models.CASCADE, related_name="my_comments")
