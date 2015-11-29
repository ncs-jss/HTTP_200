import autofixture

# for assigning Groups - 0:No group 1:StudentGroup 2:FacultyGroup

admin = autofixture.create_one('auth.User', field_values={ 'username':'admin', 'password':'admin', 'groups':['2'], 'is_superuser': True})
adminDetail = autofixture.create_one('profiles.FacultyDetail', field_values={ 'user':admin})
autofixture.create('notices.Notice', count=10, follow_fk=True,  field_values={ 'faculty': adminDetail })

student = autofixture.create_one('auth.User', field_values={ 'username':'student', 'password':'student', 'groups':['1']})
studentDetail = autofixture.create_one('profiles.StudentDetail', field_values={ 'user':student})

for _ in range(0,10):
	testadmin = autofixture.create_one('auth.User', field_values={ 'groups':['2']})
	testadminDetail = autofixture.create_one('profiles.FacultyDetail', field_values={ 'user':testadmin})

autofixture.create('notices.Notice', count=10, follow_fk=True )

for _ in range(0,10):
	teststudent = autofixture.create_one('auth.User', field_values={ 'groups':['1']})
	teststudentDetail = autofixture.create_one('profiles.StudentDetail', field_values={ 'user':teststudent})
