from rest_framework.views import APIView
#from rest_framework import generics
#from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from private_notices.models import PrivateNotice, Notification
from private_notices.serializers import PrivateNoticeViewSerializer, UserNotificationSerializer
from rest_framework.generics import ListAPIView
from private_notices.forms import PostForm

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

class NotificationView(APIView):
	def get(self, request, user_id):
		user = user_id
		private_notices = PrivateNotice.objects.filter(reciever=user_id, notification__seen=False, notification__sent=True).order_by('-created_at')
		serializer = PrivateNoticeViewSerializer(private_notices, many=True)
		return Response(serializer.data)
