from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api.v1.views import PostCreateView, LoginAPIView

app_name = 'v1'

urlpatterns = [
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('post/create/', PostCreateView.as_view(), name='post-create')
]