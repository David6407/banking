from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is my first view!!!")

def countries(request):
    return HttpResponse("Countries view")

def cities(request):
    return HttpResponse("Cities view")

def departments(request):
    return HttpResponse("Departments view")

def users(request):
    return HttpResponse("Users view")
