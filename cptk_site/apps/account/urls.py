from django.contrib import admin
from django.urls import path, include
from account import views

app_name = 'account'

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.login, name='login'),
		path('logout/', views.signout, name='signout'),
]