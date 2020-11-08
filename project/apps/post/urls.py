from django.urls import path
from .views import PostListView, PostDetailView, PostCommentCreateView

app_name = "post"
urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("<int:pk>/", PostDetailView.as_view(), name='detail'),
    path("<int:pk>/comment-create/", PostCommentCreateView.as_view(), name='comment-create')
]
