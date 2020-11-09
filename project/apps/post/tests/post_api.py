import json
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from django.urls import reverse
from apps.user.models import UserModel, VisitorModel
from utils.test_utils import CommonAPITestCase


class PostCreateAPIView(CommonAPITestCase):
    def setUp(self):
        self.login_url = reverse('api:v1:login')
        self.url = reverse('api:v1:post-create')

    def test_visitor_cant_take_token(self):
        """ test visitor can't get a token """
        password = 12345678
        email = "visitor@gmail.com"
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
        photo = SimpleUploadedFile(photo.name, photo.read(), content_type='image/png')
        user = VisitorModel.objects.create_user(email=email, password=password, photo=photo)

        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def create_admin(self):
        """ create admin user and get his token """
        password = 12345678
        email = "example@gmail.com"
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
        photo = SimpleUploadedFile(photo.name, photo.read(), content_type='image/png')
        user = UserModel.objects.create_superuser(email=email, password=password, photo=photo)

        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_create_post_as_admin(self):
        """ test admin user can get a token,
            test form validation,
            test create a post """
        token = self.create_admin()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')

        # invalid form
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data['errors'])
        self.assertIn('content', response.data['errors'])
        self.assertIn('image', response.data['errors'])

        # valid form
        data = {
            "title": "test title",
            "content": "content",
            "image": SimpleUploadedFile(photo.name, photo.read(), content_type='image/png'),
        }

        with self.assertNumQueries(2):
            response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['title'], response.data['title'])
        self.assertEqual(data['content'], response.data['content'])

        schema = self.schemas.get_post_api_create_schema()
        self.check_fields(schema, response.data)
        self.check_fields(schema['author'], response.data['author'])
