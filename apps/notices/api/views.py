from django.contrib.auth.models import User

from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
                                       permission_classes,)
from rest_framework.response import Response

from notices.models import Notice, BookmarkedNotice
from .pagination import paginated_queryset
from .serializers import (NoticeListSerializer, NoticeCreateSerializer, BookmarkedNoticeSerializer)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated, ))
def get_notice_by_pk(request, notice_pk):
    try:
        notice = Notice.objects.get(pk=notice_pk)
        serializer = NoticeListSerializer(notice)
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
    except BaseException:
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
                response_data = serializer.data
                return paginator.get_paginated_response(response_data)
        else:
            response_data = {'error': 'username field cannot be blank !'}
            return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)
    except BaseException:
        response_data = {'error': 'The User group does not exist !'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated, ))
def create_notice(request):
    user = request.META.get('HTTP_USERNAME')
    if not user:
        response_data = {'error': 'Also add username in the header.'}
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

    user = User.objects.get(username=str(user))
    if user.groups.all()[0].name.lower == "student":
        response_data = {'error': 'Students are not allowed to create notice !'}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = NoticeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {'success': 'Notice Created Successfully!'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes((permissions.IsAuthenticated, ))
def add_starred_notice(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    data = {'user': request.user.pk, 'notice': notice.pk}
    serializer = BookmarkedNoticeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response_data = {'message': 'Notice Bookmarked Successfully!'}
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated, ))
def get_starred_notice_list(request):
    try:
        bookmark_list = BookmarkedNotice.objects.filter(user=request.user).order_by('-pinned')
        if len(bookmark_list) == 0:
            response_data = {'message': 'You have not Bookmarked any notices !'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            serializer = BookmarkedNoticeSerializer(bookmark_list, remove_fields='user', many=True)
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
    except BaseException:
        response_data = {'message': 'You have not Bookmarked any notices !'}
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['DELETE', ])
@permission_classes((permissions.IsAuthenticated, ))
def delete_starred_notice(request, notice_pk):
    try:
        notice = Notice.objects.get(pk=notice_pk)
        try:
            bookmark_notice = BookmarkedNotice.objects.filter(user=request.user, notice=notice.pk)
            bookmark_notice.delete()
            response_data = {'message': 'notice successfully unstarred !'}
            return Response(response_data, status=status.HTTP_200_OK)
        except BaseException:
            response_data = {'message': 'You have not bookmarked this notice !'}
            return Response(response_data, status=status.HTTP_200_OK)
    except BaseException:
        response_data = {'error': 'some error occured . please try again !'}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated, ))
def get_complete_starred_notice_list(request):
    try:
        bookmark_list = BookmarkedNotice.objects.filter(user=request.user).order_by('-pinned')
        notice = list()
        notices = list()
        for notice_id in range(0, len(bookmark_list)):
            notice.append(bookmark_list[notice_id].notice_id)

        for notice in notice:
            notice = Notice.objects.get(pk=notice)
            notices.append(notice)

        if len(notices) == 0:
            response_data = {'message': 'You have not bookmarked any notice !'}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            paginator, result_page = paginated_queryset(notices, request)
            serializer = NoticeListSerializer(result_page, many=True)
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_200_OK)
    except BaseException:
        response_data = {'message': 'You have not bookmarked any notice !'}
        return Response(response_data, status=status.HTTP_200_OK)
