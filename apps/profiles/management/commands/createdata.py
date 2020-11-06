from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from faker import Faker
from django.contrib.auth.models import User
import sys
import os
sys.path.append(os.path.join(os.path.dirname("createdata.py"), '../../..'))
from profiles.models import StudentDetail, FacultyDetail


class Command(BaseCommand):
    help = 'Create random model instances and groups for testing purposes.'

    def add_arguments(self, parser):
        parser.add_argument('--dummydata', action='store_true', help='Create dummy data')

    def handle(self, *attrs, **options):

        _, created = Group.objects.get_or_create(name='student')
        _, created = Group.objects.get_or_create(name='faculty')
        _, created = Group.objects.get_or_create(name='management')
        _, created = Group.objects.get_or_create(name='hod')
        _, created = Group.objects.get_or_create(name='others')

        if options['dummydata']:
            fake = Faker()

            # Create admin
            User.objects.create_superuser(username='admin123', email='', password='adminadmin')

            # Create 5 users of each group respectively
            groups = ['student', 'faculty', 'management', 'hod', 'others']

            for group_name in groups:
                for i in range(0, 5):
                    name = fake.name()
                    first_name = name.split(' ')[0]
                    last_name = ' '.join(name.split(' ')[-1:])
                    username = first_name[0].lower() + last_name.lower().replace(' ', '')
                    user = User.objects.create_user(username, password=username)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.is_superuser = False
                    user.email = username + "@" + last_name.lower() + ".com"
                    users_group = Group.objects.get(name=group_name)
                    users_group.user_set.add(user)
                    user.save()
                    if (str(group_name) == "student"):
                        StudentDetail.objects.create(user=user)
                    else:
                        FacultyDetail.objects.create(user=user)
