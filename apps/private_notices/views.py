# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from private_notices.models import PrivateNotice
from private_notices.serializers import PrivateNoticeViewSerializer
from rest_framework.generics import ListAPIView


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
