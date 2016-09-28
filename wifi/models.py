from django.db import models
from django.contrib.auth.models import User
from profiles.models import StudentDetail, FacultyDetail


class WifiDetail(models.Model):
    '''
    It stores information about the wifi form of all users.
    '''
    user = models.OneToOneField(User)
    laptop_mac_address = models.CharField(max_length=200, blank=False, null=False)
    mac_registered = models.BooleanField(default=False)

    created = models.DateTimeField("Created", null=True, auto_now_add=True)
    modified = models.DateTimeField("Last Modified", null=True, auto_now=True)

    def email(self):
        return "%s" % (self.user.email)

    def name(self):
        return "%s" % (self.user.first_name)

    def branch(self):
        try:
            user = User.objects.get(username=self.user)
            profile = StudentDetail.objects.get(user=user)
            return "%s" % (profile.branch)
        except:
            user = User.objects.get(username=self.user)
            profile = FacultyDetail.objects.get(user=user)
            return "%s" % (profile.department)

    def __unicode__(self):
        return "%s" % (self.user)
