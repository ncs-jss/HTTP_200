from rest_framework import permissions
from django.contrib.auth.models import User, Group


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the owner of the notice.
		return obj.owner.user == request.user


def is_in_group(user, group_name):
	"""
	Takes a user and a group name, and returns `True` if the user is in that group.
	"""
	return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()

class HasGroupPermission(permissions.BasePermission):
	"""
	Ensure user is in required groups.
	"""

	def has_permission(self, request, view):
		# Get a mapping of methods -> required group.
		required_groups_mapping = getattr(view, 'required_groups', {})

		# Determine the required groups for this particular request method.
		required_groups = required_groups_mapping.get(request.method, [])

		# Return True if the user has all the required groups.
		return all([is_in_group(request.user, group_name) for group_name in required_groups])

class IsOwnerOrReadOnlyUser(permissions.BasePermission):
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

class IsAuthenticatedUser(permissions.BasePermission):
	"""
	Custom permission for userserializer for an object to edit the details.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the owner of the snippet.
		return obj == request.user
