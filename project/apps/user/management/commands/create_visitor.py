from django.core.management.base import BaseCommand
from apps.user.models import VisitorModel


class Command(BaseCommand):
    """ create visitor user """
    help = 'Enter email and password to create a super user'

    def handle(self, *args, **options):
        user_attrs = dict()
        user_attrs['email'] = input('email: ')
        user_attrs['password'] = input('password: ')
        VisitorModel.objects.create_user(**user_attrs)
