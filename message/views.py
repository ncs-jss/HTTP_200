from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from message.models import Message, Notification
from message.serializers import MessageViewSerializer
from rest_framework.generics import ListAPIView

class MessageView(ListAPIView):
	queryset = Message.objects.all()
	serializer_class = MessageViewSerializer
