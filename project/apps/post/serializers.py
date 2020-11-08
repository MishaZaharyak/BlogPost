from rest_framework import serializers
from apps.post.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    author = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = "__all__"

    def get_author(self, obj):
        return str(obj.author)
