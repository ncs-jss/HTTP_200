from rest_framework.permissions import (
    AllowAny,
)
from django.contrib.auth import get_user_model
from .serializers import (
    UserLoginSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

User = get_user_model()


class UserLoginAPIView(APIView):
    """
    API to obtain the token from username and password of the user.
    """
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = serializer.errors
            return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)
