from rest_framework import serializers
from apps.post.models import PostModel
from apps.user.serializers import UserSerializer


class PostWriteSerializer(serializers.ModelSerializer):
    """ Post model write serializer """
    class Meta:
        model = PostModel
        fields = '__all__'
        read_only_fields = ['author']

    @property
    def data(self):
        """ put author data to serializer data """
        data = super().data
        author = UserSerializer(self.instance.author, context=self.context).data
        return {**data, 'author': author}
