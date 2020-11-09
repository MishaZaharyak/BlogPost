from rest_framework.response import Response
from rest_framework.test import APITestCase
from apps.post.tests.schemas import PostViewSchemas


class Schemas(PostViewSchemas):
    pass


class CommonAPITestCase(APITestCase):

    def __init__(self, *args, **kwargs):
        super(CommonAPITestCase, self).__init__(*args, **kwargs)
        self.schemas = Schemas()

    def check_fields(self, fields, response):
        self.assertEqual(len(fields), len(response))
        self.assertTrue(all([field in response for field in fields]))

    @staticmethod
    def get_non_field_error(response: Response) -> str:
        return response.data['errors']['non_field_errors'][0]
