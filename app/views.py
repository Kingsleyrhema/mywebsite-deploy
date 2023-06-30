from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about_us(request):
    return render(request, 'app/about-us.html')

def services(request):
    return render(request, 'app/services.html')

def projects(request):
    return render(request, 'app/projects.html')

def contact(request):
    return render(request, 'app/contact.html')