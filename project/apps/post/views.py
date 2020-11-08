from django.http import HttpResponseRedirect
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.post.models import PostModel
from apps.post.serializers import PostListSerializer, PostDetailSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import generics, views, status
from .forms import PostCommentForm
from django.shortcuts import reverse


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        comment_form = PostCommentForm()
        return Response({**serializer.data, 'comment_form': comment_form})


class PostCommentCreateView(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]
    template_name = "post/detail.html"
    form = PostCommentForm

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            visitor = request.user.visitormodel
            form.save(author=visitor, post_id=kwargs['pk'])
            return HttpResponseRedirect(redirect_to=reverse('post:detail', args=[kwargs['pk']]))
        else:
            return Response({"comment_form": form}, status=status.HTTP_400_BAD_REQUEST)
