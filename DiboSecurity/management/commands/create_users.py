import datetime

import pytz
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create specific users'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        # @formatter:off
        #User.objects.create_user(username='admin', password='Kode1234!', first_name='', last_name='', email='', is_superuser=True, is_staff=True, is_active=True, date_joined=datetime.datetime.today())
        User.objects.create_user(username='tobias', password='Kode1234!',   first_name='', last_name='', email='', is_superuser=True,  is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='steffen', password='Kode1234!',  first_name='', last_name='', email='', is_superuser=False, is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='niels', password='Kode1234!',    first_name='', last_name='', email='', is_superuser=False, is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='lars', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='jeho', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='jaal', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='nian', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=True,  is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='taje', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=False, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='joni', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=False, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='dexa', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=False, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='kaab', password='Kode1234!',     first_name='', last_name='', email='', is_superuser=False, is_staff=False, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        # @formatter:on

    # def create_username_from_name(self,first_name,last_name):
    #     first_name[0:3] + last_name[0:2]
