from django import forms

from apps.post.models import PostModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ('author', "created_at", "updated_at")
