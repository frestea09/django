from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'^$',views.index,name='main_introduction_view'),
]