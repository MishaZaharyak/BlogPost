from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.v1.permissions import IsSuperUser
from api.v1.serializers import PostWriteSerializer
from apps.post.models import PostModel


class PostCreateView(generics.CreateAPIView):
    queryset = PostModel.objects.all()
    permission_classes = [IsAuthenticated, IsSuperUser]
    serializer_class = PostWriteSerializer

    def get_queryset(self):
        return super().get_queryset().select_related('author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
