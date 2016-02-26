from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from permissions import IsPrivateNoticeOwner
from rest_framework.response import Response
from private_notices.models import PrivateNotice, Notification
from private_notices.serializers import PrivateNoticeViewSerializer, UserNotificationSerializer
from rest_framework.generics import ListAPIView
from private_notices.forms import PostForm
from django.contrib.auth.models import User


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
	permission_classes = (IsAuthenticated,IsPrivateNoticeOwner,)

	def get(self, request, user_id):
		try:
			user = User.objects.get(id=user_id)
			print user.username
		except:
			return Response("User does not exists")

		self.check_object_permissions(request, user)
		private_notices = PrivateNotice.objects.filter(reciever=user_id, notification__seen=False, notification__sent=True).order_by('-created_at')
		serializer = PrivateNoticeViewSerializer(private_notices, many=True)
		return Response(serializer.data)
