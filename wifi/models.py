from django.db import models
from django.contrib.auth.models import User
from profiles.models import StudentDetail, FacultyDetail


class WifiDetail(models.Model):
    '''
    It stores information about the wifi form of all users.
    '''
    user = models.OneToOneField(User)
    laptop_mac_address = models.CharField(max_length=200, blank=False, null=False)

    created = models.DateTimeField("Created", null=True, auto_now_add=True)
    modified = models.DateTimeField("Last Modified", null=True, auto_now=True)

    def user_email(self):
    	return self.user.email

    def user_name(self):
    	return self.user.first_name

    def __unicode__(self):
        return "%s" % (self.user)
