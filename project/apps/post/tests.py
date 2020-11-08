import json

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import tag
from django.urls import reverse
from apps.user.models import UserModel


class PostCreateAPIView(APITestCase):
    def setUp(self):
        self.login_url = reverse('api:v1:login')
        self.url = reverse('api:v1:post-create')

    def create_admin(self):
        password = 12345678
        email = "example@gmail.com"
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
        photo =  SimpleUploadedFile(photo.name, photo.read(), content_type='image/png')
        user = UserModel.objects.create_superuser(email=email, password=password, photo=photo)

        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_create_post_as_admin(self):
        token = self.create_admin()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
        data = {
            "title": "test title",
            "content": "content",
            "image": SimpleUploadedFile(photo.name, photo.read(), content_type='image/png'),
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['title'], response.data['title'])
        self.assertEqual(data['content'], response.data['content'])
        self.assertIn('author', response.data)
        self.assertIn('email', response.data['author'])
        self.assertIn('first_name', response.data['author'])
        self.assertIn('last_name', response.data['author'])
        self.assertIn('photo', response.data['author'])
        self.assertIn('id', response.data['author'])
