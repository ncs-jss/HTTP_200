from django.core.management.base import BaseCommand, CommandError
import autofixture

admin_md5 = '21232f297a57a5a743894a0e4a801fc3'
student_md5 = 'cd73502828457d15655bbd7a63fb0bc8'
default_md5 = 'c21f969b5f03d33d43e04f8f136e7682'

class Command(BaseCommand):
    help = 'Create random model instances for testing purposes.'
    

    def add_arguments(self, parser):
        pass

    def handle(self, *attrs, **options):
        
        # for assigning Groups - 0:No group 1:StudentGroup 2:FacultyGroup
        admin = autofixture.create_one('auth.User', field_values={ 'username':'admin', 'password':admin_md5, 'groups':['2'], 'is_superuser': True})
        adminDetail = autofixture.create_one('profiles.FacultyDetail', field_values={ 'user':admin})
        autofixture.create('notices.Notice', count=10, follow_fk=True,  field_values={ 'faculty': adminDetail })

        student = autofixture.create_one('auth.User', field_values={ 'username':'student', 'password':student_md5, 'groups':['1']})
        studentDetail = autofixture.create_one('profiles.StudentDetail', field_values={ 'user':student})

        for _ in range(0,10):
            testadmin = autofixture.create_one('auth.User', field_values={'password':default_md5, 'groups':['2']})
            testadminDetail = autofixture.create_one('profiles.FacultyDetail', field_values={ 'user':testadmin})

        autofixture.create('notices.Notice', count=10, follow_fk=True )

        for _ in range(0,10):
            teststudent = autofixture.create_one('auth.User', field_values={'password':default_md5, 'groups':['1']})
            teststudentDetail = autofixture.create_one('profiles.StudentDetail', field_values={ 'user':teststudent})
