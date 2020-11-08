from rest_framework import serializers
from apps.post.models import PostModel, PostCommentModel
from apps.user.serializers import UserSerializer


class GetAuthorMixin:
    def get_author(self, obj):
        return str(obj.author)


class PostListSerializer(GetAuthorMixin, serializers.ModelSerializer):
    """ Post model list serializer """
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    author = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = "__all__"


class PostCommentSerializer(GetAuthorMixin, serializers.ModelSerializer):
    """ Post Comment model serializer """

    class Meta:
        model = PostCommentModel
        exclude = ('post',)


class PostDetailSerializer(PostListSerializer):
    """ Post model detail serializer """
    author = UserSerializer()
    comments = PostCommentSerializer(many=True)
