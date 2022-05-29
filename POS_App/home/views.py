from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('This app will be used for startup nagivation')

def login(request):
	return HttpResponse('sadie todo')
