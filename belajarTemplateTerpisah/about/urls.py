from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name='about_main_view')
]