from django.urls import path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import re_path
from . import views
def index(request):
    return HttpResponse("Ini index")
def about(request):
    return HttpResponse("Ini About")
def client(request):
    return HttpResponse('Ini client')
def error(request):
    return HttpResponse("Hayo mau ngapain")
urlpatterns = [
    path('', index, name='main-view'),
    path('about/',about, name='about-view'),
    path('client/',client, name='client-view'),
    re_path(r'^$',error,name='Error view'),

]