from django.contrib.auth.models import User

from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       permission_classes,)
from rest_framework.response import Response

from notices.models import Notice
from .pagination import paginated_queryset
from .serializers import (NoticeListSerializer, NoticeCreateSerializer,)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated, ))
def get_notice_by_pk(request, notice_pk):
    try:
        notice = Notice.objects.get(pk=notice_pk)
        serializer = NoticeListSerializer(notice)
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
    except:
        response_data = {'error': 'Notice does not exist !'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated, ))
def get_notice_by_list(request):
    try:
        user_group = request.user.groups.all()[0].name.lower()
        notices = Notice.objects.filter(**{'visible_for_'+user_group: True})
        category = request.META.get('HTTP_CATEGORY')
        username = request.META.get('HTTP_USERNAME')
        if username:
            if category is None:
                notices = notices.order_by('-modified')
                paginator, result_page = paginated_queryset(notices, request)
                serializer = NoticeListSerializer(result_page, many=True)
                response_data = serializer.data
                return paginator.get_paginated_response(response_data)
            else:
                notices = notices.filter(category=category).order_by('-modified')
                paginator, result_page = paginated_queryset(notices, request)
                serializer = NoticeListSerializer(result_page, many=True)
                print serializer.data
                response_data = serializer.data
                return paginator.get_paginated_response(response_data)
        else:
            response_data = {'error': 'username field cannot be blank !'}
            return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)
    except:
        response_data = {'error': 'The User group does not exist !'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated, ))
def create_notice(request):
    user = request.META.get('HTTP_USERNAME')
    print "user", type(user)
    user = User.objects.get(username=str(user))
    if user.groups.all()[0].name.lower == "student":
        response_data = {'error': 'Students are not allowed to create notice !'}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            serializer = NoticeCreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class NoticeCreateViewSet(APIView):
#     queryset = Notice.objects.all()
#     serializer_class = NoticeCreateSerializer
#     permission_classes = [IsAuthenticated, ]
#     parser_classes = (MultiPartParser, FormParser,)

#     def post(self, request):
#         user = self.request.META.get('HTTP_USERNAME')
#         user = User.objects.filter(username=user)[0]
#         if user.groups.all()[0].name.lower() == "student":
#             raise ValidationError({"error": "Student Can't create notice."})
#         else:
#             try:
#                 serializer = NoticeCreateSerializer(data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 return Response(serializer.data, status=HTTP_200_OK)
#             except:
#                 return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
