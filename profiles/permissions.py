from rest_framework import permissions
from django.contrib.auth.models import User, Group


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
