from django.db import models
from django.contrib.auth.models import User


class EmailDetail(models.Model):
    '''
    It stores information about the email form of all users.
    '''
    user = models.OneToOneField(User)
    email_purpose = models.TextField(max_length=200,
                                     blank=True,
                                     null=True,
                                     default=None)
    attachment = models.FileField(upload_to='forms/email/',
                                  blank=True,
                                  null=True)
    hod_approved_email = models.BooleanField(default=False)

    created = models.DateTimeField("Created", null=True, auto_now_add=True)
    modified = models.DateTimeField("Last Modified", null=True, auto_now=True)

    def email(self):
        return "%s" % (self.user.email)

    def name(self):
        return "%s" % (self.user.first_name)

    def __unicode__(self):
        return "%s" % (self.user)
