from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('create-user/', views.create_user, name='create-user')
]
