from django.core.management.base import BaseCommand, CommandError
import autofixture
import logging
logger = logging.getLogger(__name__)


admin_md5 = '21232f297a57a5a743894a0e4a801fc3'
student_md5 = 'cd73502828457d15655bbd7a63fb0bc8'
default_md5 = 'c21f969b5f03d33d43e04f8f136e7682'

class Command(BaseCommand):
	help = 'Create random model instances for testing purposes.'
	

	def add_arguments(self, parser):
		pass

	def handle(self, *attrs, **options):
		
		# for assigning Groups - 
		#   0:No group 
		#   1:StudentGroup 
		#   2:FacultyGroup
		logger.debug("Creating a Faculty Superuser with username: admin and password %s" %admin_md5)
		admin = autofixture.create_one('auth.User',
			field_values={ 'username':'admin',
				'password':admin_md5,
				'groups':['2'],
				'is_superuser': True,
				})

		adminDetail = autofixture.create_one('profiles.FacultyDetail',
			field_values={
				'user':admin
				})

		logger.debug("Creating 10 Notices")
		autofixture.create('notices.Notice',
			count=10,
			follow_fk=True,
			field_values={
				'faculty': adminDetail
				})

		logger.debug("Creating Student type User with username 'student' and password %s" %student_md5)
		student = autofixture.create_one('auth.User',
			field_values={
				'username':'student',
				'password':student_md5,
				'groups':['1'],
				'is_superuser': True,
				})

		studentDetail = autofixture.create_one('profiles.StudentDetail',
			field_values={
				'user':student
				})

		logger.debug("Creating 10 random Faculty Accounts")
		for _ in xrange(0,10):
			test_faculty = autofixture.create_one('auth.User',
				field_values={
					'password':default_md5,
					'groups':['2']
					})
			test_faculty_detail = autofixture.create_one('profiles.FacultyDetail',
				field_values={
					'user':test_faculty
					})

		logger.debug("Creating 10 random Notices")
		autofixture.create('notices.Notice', count=10, follow_fk=True )

		logger.debug("Creating 10 random Student Accounts")
		for _ in range(0,10):
			test_student = autofixture.create_one('auth.User',
				field_values={
					'password':default_md5,
					'groups':['1']
					})
			test_student_detail = autofixture.create_one('profiles.StudentDetail',
				field_values={
					'user':test_student
					})
