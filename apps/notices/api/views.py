from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       permission_classes,)
from rest_framework.response import Response

from notices.models import Notice
from .serializers import (NoticeListSerializer,)


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

# class NoticeListViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated, ]
#     pagination_class = NoticePageNumberPagination
#     serializer_class = NoticeListSerializer
#     def get_queryset(self, **kwargs):
#         user_group = self.request.user.groups.all()[0].name.lower()
#         notices = Notice.objects.filter(**{'visible_for_'+user_group: True})
#         category = self.request.META.get('HTTP_CATEGORY')
#         username = self.request.META.get('HTTP_USERNAME')
#         try:
#             notice_id = self.kwargs["pk"]
#         except:
#             notice_id = None
#         if notice_id:
#             queryset = Notice.objects.filter(pk=notice_id)
#             return queryset

#         else:
#             if username:
#                 if category == "none":
#                     queryset = notices.order_by('-modified')
#                     return queryset
#                 elif category == "":
#                     raise ValidationError({"category": "This field can't be left blank."})
#                 else:
#                     queryset = notices.filter(category=category).order_by('-modified')
#                     return queryset
#             else:
#                 raise ValidationError({"username": "This field can't be left blank."})
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
