from django.contrib.auth.models import User
from django.db import models


class FirebaseToken(models.Model):
    """
    It stores the firebase id with corresponding users.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firebase_token = models.CharField(max_length=200, blank=False, null=False)


class NotificationPreference(models.Model):
    """
    It stores the user Preferences with corresponding users.
    Starting from left to right the order is given below.
    """
    # 0 - Academics
    # 0 - Administration
    # 0 - Tnp
    # 0 - Events
    # 0 - Misc
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    notification_preferences = models.CharField(max_length=5, blank=False, null=False, default='00000')
