from django.contrib.auth.models import Group
from djangorestframework.permissions import _403_FORBIDDEN_RESPONSE, BasePermission

# class GroupBasePermission(BasePermission):

# 	group_name = ""

# 	def check_permission(self, user):

# 		try:
# 			user_group = user.groups.get(name=self.group_name)
# 			return user_group
# 		except:
# 			raise _403_FORBIDDEN_RESPONSE

# class GroupAPIPOSTPermission(GroupAPIPOSTPermission):
# 	"""
# 	Checks to see if a user is in a particular group.
# 	"""
# 	group_name = "student"


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
