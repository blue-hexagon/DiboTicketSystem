import datetime

import pytz
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create specific users'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        # @formatter:off
        # User.objects.create_user(username='admin', password='Kode1234!', first_name='', last_name='', email='', is_superuser=True, is_staff=True, is_active=True, date_joined=datetime.datetime.today())
        User.objects.create_user(username='tobi802j', password='Kode1234!', first_name='Tobias',  last_name='Larsen',   email='tobi802j@zbc.dk', is_superuser=False, is_staff=True, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='stef12e',  password='Kode1234!', first_name='Steffen', last_name='Henriksen',email='stef12e@zbc.dk',  is_superuser=False, is_staff=True, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='tobi801j', password='Kode1234!', first_name='Tobias',  last_name='Andersen', email='tobi801j@zbc.dk', is_superuser=True,  is_staff=True, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        User.objects.create_user(username='mort83f',  password='Kode1234!', first_name='Morten',  last_name='Modig',    email='mort83f@zbc.dk',  is_superuser=False, is_staff=True, is_active=True, date_joined=datetime.datetime(2023, 3, 1, 12, 8, 7, 000000, tzinfo=pytz.UTC))
        # @formatter:on

