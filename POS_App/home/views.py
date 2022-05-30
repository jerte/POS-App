from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
	return HttpResponse('This app will be used for startup nagivation')

def login(request):
	return HttpResponse('sadie todo')

def create_user(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			auth_login(request, user)
			return redirect('index')
		else:
			return render(request, 'add_user.html', {'form':form})
	else:
		form = UserCreationForm()
		return render(request, 'add_user.html', {'form':form})
