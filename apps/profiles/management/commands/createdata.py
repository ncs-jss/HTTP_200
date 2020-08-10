from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
import autofixture
import logging
import hashlib
logger = logging.getLogger(__name__)


# admin_md5 = '21232f297a57a5a743894a0e4a801fc3'
# student_md5 = 'cd73502828457d15655bbd7a63fb0bc8'
# default_md5 = 'c21f969b5f03d33d43e04f8f136e7682'

admin_md5 = hashlib.md5('admin').hexdigest()
student_md5 = hashlib.md5('student').hexdigest()
default_md5 = hashlib.md5('default').hexdigest()


class Command(BaseCommand):
    help = 'Create random model instances for testing purposes.'

    def add_arguments(self, parser):
        pass

    def handle(self, *attrs, **options):

        _, created = Group.objects.get_or_create(name='student')
        _, created = Group.objects.get_or_create(name='faculty')
        _, created = Group.objects.get_or_create(name='management')
        _, created = Group.objects.get_or_create(name='hod')
        _, created = Group.objects.get_or_create(name='others')

        # for assigning Groups -
        #   0:No group
        #   1:student
        #   2:faculty
        logger.debug("Creating a Faculty Superuser with username: admin and password %s" % admin_md5)
        admin = autofixture.create_one('auth.User',
                                       field_values={'username': 'admin',
                                                     'password': admin_md5,
                                                     'groups': ['2'],
                                                     'is_superuser': True,
                                                     })

        adminDetail = autofixture.create_one('profiles.FacultyDetail',
                                             field_values={
                                                 'user': admin
                                             })

        logger.debug("Creating 10 Notices")
        autofixture.create('notices.Notice',
                           count=10,
                           follow_fk=True,
                           field_values={
                               'faculty': adminDetail
                           })

        logger.debug("Creating Student type User with username 'student' and password %s" % student_md5)
        student = autofixture.create_one('auth.User',
                                         field_values={
                                             'username': 'student',
                                             'password': student_md5,
                                             'groups': ['1'],
                                             'is_superuser': True,
                                         })

        autofixture.create_one('profiles.StudentDetail', field_values={'user': student})

        logger.debug("Creating 10 random Faculty Accounts")
        for _ in xrange(0, 10):
            test_faculty = autofixture.create_one('auth.User',
                                                  field_values={
                                                      'password': default_md5,
                                                      'groups': ['2']
                                                  })
            autofixture.create_one('profiles.FacultyDetail', field_values={'user': test_faculty})

        logger.debug("Creating 10 random Notices")
        autofixture.create('notices.Notice', count=10, follow_fk=True)

        logger.debug("Creating 10 random Student Accounts")
        for _ in range(0, 10):
            test_student = autofixture.create_one('auth.User',
                                                  field_values={
                                                      'password': default_md5,
                                                      'groups': ['1']
                                                  })
            autofixture.create_one('profiles.StudentDetail', field_values={'user': test_student})
