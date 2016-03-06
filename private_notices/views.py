from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from permissions import IsPrivateNoticeOwner
from rest_framework.response import Response
from private_notices.models import PrivateNotice, Notification
from private_notices.serializers import PrivateNoticeViewSerializer, UserNotificationSerializer
from rest_framework.generics import ListAPIView
from private_notices.forms import PostForm
from django.contrib.auth.models import User
from django.views.generic import View
from django.views import generic
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PrivateNoticeView(ListAPIView):
    queryset = PrivateNotice.objects.all()
    serializer_class = PrivateNoticeViewSerializer

'''
class CreatePrivateNoticeView(APIView):
    def get(self, request):
        user = request.Get.get('userid')
        form = PostForm()
        return Response({'form':form})
    
    def post(self, request):
        user = request.data.get('userid')
        return "form"
'''

class NotificationView(generic.View):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        template = 'private_notices/list.html'
        try:
            user = User.objects.get(id=user_id)
        except:
            return Response("User does not exists")

        if self.request.user == user:
            private_notices = PrivateNotice.objects.filter(reciever=user_id, notification__seen=False, notification__sent=True).order_by('-created_at')
            paginator = Paginator(private_notices, 10)
            page = request.GET.get('page')
            try:
                notices = paginator.page(page)
            except PageNotAnInteger:
                notices = paginator.page(1)
            except EmptyPage:
                notices = paginator.page(paginator.num_pages)       

            return render(request, template, {"private_notices": notices})
        else:
            raise PermissionDenied()