from django.shortcuts import render
from django.http import *
from couchbase.bucket import Bucket

cb = Bucket('couchbase:///infodb', password="123456")
print cb

def home(request):
	return HttpResponse("Hi there. It is working very fine.")