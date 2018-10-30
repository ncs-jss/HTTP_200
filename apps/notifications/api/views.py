from django.contrib.auth.models import User

from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       permission_classes,)
from rest_framework.response import Response

from notifications.models import NotificationPreference
from .serializers import FirebaseTokenSerializer, NotificationPreferenceSerializer


@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
def set_firebase_token(request):
    serializer = FirebaseTokenSerializer(data=request.data)
    if long(request.data['user_id']) == long(request.user.pk):
        if serializer.is_valid():
            serializer.save()
            user_id = User.objects.get(pk=request.user.pk)
            NotificationPreference.objects.create(user_id=user_id)
            response_data = {'success': 'The Firebase token is successfully registered.'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        response_data = {'error': 'User id is not correct !'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST', 'GET', ])
@permission_classes((permissions.IsAuthenticated,))
def notification_preference(request):
    if request.method == "POST":
        try:
            user_preference = NotificationPreference.objects.get(user_id=request.data['user_id'])
        except NotificationPreference.DoesNotExist:
            response_data = {'error': 'you have not registered firebase token !'}
            return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = NotificationPreferenceSerializer(user_preference, data=request.data)
        if long(request.data['user_id']) == long(request.user.pk):
            if serializer.is_valid():
                serializer.save()
                response_data = {'success': 'The notification preference has been successfully saved.'}
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == 'GET':
        user_id = request.META.get('HTTP_USERID')
        try:
            notification = NotificationPreference.objects.get(user_id=user_id)
            serializer = NotificationPreferenceSerializer(notification)
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
        except BaseException:
            response_data = {'error': 'you have not registered firebase token !'}
            return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)
