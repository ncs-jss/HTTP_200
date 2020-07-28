from django.db import models
from django.contrib.auth.models import User
from profiles.models import StudentDetail, FacultyDetail
from django.core.validators import RegexValidator


class WifiDetail(models.Model):
    '''
    It stores information about the wifi form of all users.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    old_laptop_mac_address = models.CharField(max_length=200,
                                              blank=False,
                                              null=False,
                                              default=None,
                                              validators=[RegexValidator(regex='^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$', message='Enter MAC Address in Given Format.'), ])
    new_laptop_mac_address = models.CharField(max_length=200,
                                              blank=True,
                                              null=True,
                                              default=None,
                                              validators=[RegexValidator(regex='^([0-9A-F]{2}[:]){5}([0-9A-F]{2})$', message='Enter MAC Address in Given Format.'), ])
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
        except BaseException:
            user = User.objects.get(username=self.user)
            profile = FacultyDetail.objects.get(user=user)
            return "%s" % (profile.department)

    def __unicode__(self):
        return "%s" % (self.user)
