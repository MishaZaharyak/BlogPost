from django import forms
from apps.post.models import PostModel, PostCommentModel
from apps.user.models import VisitorModel


class PostForm(forms.ModelForm):
    """ Post admin form """
    class Meta:
        model = PostModel
        exclude = ('author', "created_at", "updated_at")


class PostCommentForm(forms.ModelForm):
    """ Post comment admin form """
    class Meta:
        model = PostCommentModel
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }

    def save(self, commit=True, author: VisitorModel = None, post_id: int = None):
        """ save passing author and post with given comment """
        comment = super().save(commit=False)
        comment.author = author
        comment.post_id = post_id
        if commit:
            comment.save()
        return comment
