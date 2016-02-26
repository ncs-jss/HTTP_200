from rest_framework import permissions
from django.contrib.auth.models import User
from private_notices.models import PrivateNotice, Notification

class IsPrivateNoticeOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and obj == request.user:
            return True
