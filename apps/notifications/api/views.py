from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       permission_classes,)
from rest_framework.response import Response

from .serializers import FirebaseTokenSerializer


@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated,))
def set_firebase_token(request):
    serializer = FirebaseTokenSerializer(data=request.data)
    if long(request.data['user_id']) == long(request.user.pk):
        if serializer.is_valid():
            serializer.save()
            response_data = {'success': 'The Firebase token is successfully registered.'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        response_data = {'error': 'User id is not correct !'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)
