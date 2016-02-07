from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class PrivateNotice(models.Model):
    sender = models.ForeignKey(User, related_name='Sender')
    reciever = models.ForeignKey(User, related_name='Reciever')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='PrivateNotice Date')
    # can send PrivateNotices only not emails
    pnotice = models.CharField(max_length=500, help_text="Please restrict the PrivateNotice length to 500.")

    def __str__(self):
        return self.pnotice

# Autopopulation of seen field needed while creating PrivateNotices
# to ensure the sent status


class Notification(models.Model):
    '''
    Notification is populated at same time the PrivateNotice is created.
    Only seen and seen_at is left as it is
    '''
    mid = models.ForeignKey(PrivateNotice, verbose_name='PrivateNotice Id', related_name='notification')
    sent = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)  # True when reciever clicks on the Notification
    seen_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return str(self.seen)
