from django.urls import path
from django.contrib import  admin
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Welcome to Home</h1>")
def about(request):
    return HttpResponse("<h1>ini adalah about</h1>")