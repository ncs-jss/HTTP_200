from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       permission_classes,)
from rest_framework.response import Response

from profiles.models import StudentDetail
from .serializers import (UserLoginSerializer, StudentProfileSerializer)


@api_view(['POST', ])
@permission_classes((permissions.AllowAny, ))
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET', 'PUT', 'PATCH', ])
@permission_classes((permissions.IsAuthenticated, ))
def student_profile_data(request, user_id):
    try:
        student_detail = StudentDetail.objects.get(pk=user_id)
    except StudentDetail.DoesNotExist:
        response_data = {'error': 'User does not exist'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method == 'GET':
        student_detail = StudentDetail.objects.get(pk=user_id)
        serializer = StudentProfileSerializer(student_detail)
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method in ['PUT', 'PATCH']:
        if request.method == 'PATCH':
            serializer = StudentProfileSerializer(student_detail, data=request.data, partial=True)
        else:
            serializer = StudentProfileSerializer(student_detail, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response_data = {'success': 'Profile Successfully updated!'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
