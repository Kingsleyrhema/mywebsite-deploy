from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from . import views
from django.contrib.auth.views import LoginView

appname = 'app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('/about_us', views.about_us, name='about'),
    path('/services', views.services, name='services'),
    path('/projects', views.projects, name='projects'),
    path('/contact us', views.contact, name='contact'),
]