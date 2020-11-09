import json
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from django.test import tag
from django.urls import reverse
from apps.user.models import UserModel, VisitorModel
from utils.test_utils import CommonAPITestCase


class PostViewsTest(CommonAPITestCase):
    def setUp(self):
        self.list_url = reverse('post:list')
        self.login_url = reverse('api:v1:login')
        self.post_create = reverse('api:v1:post-create')
        self.create_posts()

    def create_posts(self):
        """ create admin user and few post """
        password = 12345678
        email = "example@gmail.com"
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
        photo = SimpleUploadedFile(photo.name, photo.read(), content_type='image/png')
        user = UserModel.objects.create_superuser(email=email, password=password, photo=photo)

        data = {
            'email': email,
            'password': password
        }
        self.admin_creds = data
        response = self.client.post(self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.admin_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")

        titles = ["Cars", "onion", "People", "Dresses", "Food", "Job", "Vacancies"]

        for title in titles:
            photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
            photo = SimpleUploadedFile(photo.name, photo.read(), content_type='image/png')

            data = {
                "title": title,
                "content": """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus aliquam""",
                "image": photo,
            }

            with self.assertNumQueries(2):
                response = self.client.post(self.post_create, data=data)

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        """ test public post list view """
        self.client.credentials()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        schema = self.schemas.get_post_list_schema()
        self.check_fields(schema, response.data)
        self.check_fields(schema['results'][0], response.data['results'][0])
        self.assertEqual(len(response.data['results']), 5)

    @tag('detail')
    def test_public_post_detail_view(self):
        """ test get public post detail data """
        self.client.credentials()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_id = response.data['results'][0]['id']

        # get post
        post_detail_url = reverse('post:detail', args=[post_id])

        with self.assertNumQueries(2):
            response = self.client.get(post_detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        schema = self.schemas.get_post_detail_schema()
        self.check_fields(schema, response.data)
        self.check_fields(schema['author'], response.data['author'])

    @tag('comment')
    def test_create_comment(self):
        self.client.credentials()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post_id = response.data['results'][0]['id']
        # not authenticated
        comment_url = reverse('post:comment-create', args=[post_id])
        response = self.client.post(comment_url, data={})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not Visitor user
        self.client.login(**self.admin_creds)
        response = self.client.post(comment_url, data={})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # not valid form
        password = 12345678
        email = "visitor@gmail.com"
        photo = open(f"{settings.BASE_DIR}/staticfiles/img/No-photo-m.png", 'rb')
        photo = SimpleUploadedFile(photo.name, photo.read(), content_type='image/png')
        user = VisitorModel.objects.create_user(email=email, password=password, photo=photo)
        data = {
            'email': email,
            'password': password
        }
        self.client.login(**data)
        response = self.client.post(comment_url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # valid form
        with self.assertNumQueries(4):
            response = self.client.post(comment_url, data={"text": 'some text'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        with self.assertNumQueries(4):
            response = self.client.post(comment_url, data={"text": 'some new text'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        with self.assertNumQueries(4):
            response = self.client.post(comment_url, data={"text": 'weather'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get post
        post_detail_url = reverse('post:detail', args=[post_id])

        with self.assertNumQueries(6):
            response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        schema = self.schemas.get_post_detail_schema()
        self.check_fields(schema, response.data)
        self.check_fields(schema['comments'][0], response.data['comments'][0])


