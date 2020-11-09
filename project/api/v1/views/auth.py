from django.contrib.auth import get_user_model
from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from api.v1.serializers.auth import LoginSerializer
from utils.utils import create_error


class LoginAPIView(views.APIView):
    """ Login View for API """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        1) validate request data
        2) find user with requested email, and check it password
        3) return refresh and access token for that user
        """
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        error_msg = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
        serialized_data = serializer.data
        email = serialized_data.get('email')
        password = serialized_data.get('password')

        user_model = get_user_model()

        try:
            user = user_model.objects.get(email=email, is_active=True, is_superuser=True)
        except user_model.DoesNotExist:
            return Response(data=create_error(error_msg), status=status.HTTP_403_FORBIDDEN)

        if user is None or not user.check_password(password):
            return Response(data=create_error(error_msg), status=status.HTTP_403_FORBIDDEN)

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data=data, status=status.HTTP_200_OK)
