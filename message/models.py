from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Message(models.Model):
	sender = models.OneToOneField(User, related_name='Sender')
	reciever = models.OneToOneField(User, related_name='Reciever')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Message Date')
	message = models.CharField(max_length=500, help_text="Please restrict the message length to 500.") #can send messages only not emails

	def __str__(self):
		return self.message

class Notification(models.Model):
	'''
	Notification is populated at same time the Message is created.
	Only seen and seen_at is left as it is
	'''
	mid = models.ForeignKey(Message, verbose_name='Message Id')
	sent = models.BooleanField(default = True)
	seen = models.BooleanField(default = False) #True when reciever clicks on the Notification
	seen_at = models.DateTimeField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return str(self.seen)
