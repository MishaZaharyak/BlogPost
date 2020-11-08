from django.core.management.base import BaseCommand
from apps.user.models import UserModel


class Command(BaseCommand):
    help = 'Enter email and password to create a super user'

    def handle(self, *args, **options):
        user_attrs = dict()
        user_attrs['email'] = input('email: ')
        user_attrs['password'] = input('password: ')
        UserModel.objects.create_superuser(**user_attrs)
