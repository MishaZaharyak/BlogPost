from rest_framework.permissions import AllowAny
from apps.post.models import PostModel
from apps.post.serializers import PostListSerializer, PostDetailSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics


class PostListView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset().select_related("author")

    def get_paginated_response(self, data):
        """
        Return a paginated style object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response_obj(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return Response(self.get_paginated_response(serializer.data), template_name="post/list.html")


class PostDetailView(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [AllowAny]
    template_name = "post/detail.html"
