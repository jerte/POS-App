from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	return HttpResponse('This app will be used for taking orders from customers and recording transactions')
