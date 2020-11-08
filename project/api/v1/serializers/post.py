from rest_framework import serializers
from apps.post.models import PostModel
from apps.user.serializers import UserSerializer


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        read_only_fields = ['author']

    @property
    def data(self):
        data = super().data
        author = UserSerializer(self.instance.author, context=self.context).data
        return {**data, 'author': author}
