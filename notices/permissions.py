from rest_framework import permissions
from django.contrib.auth.models import User, Group


class IsNoticeOwner(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the owner of the snippet.
		return obj.user == request.user

def is_in_group(user, group_name):
	"""
	Takes a user and a group name, and returns `True` if the user is in that group.
	"""
	return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
