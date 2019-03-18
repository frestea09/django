from django.urls import path,re_path
from . import views
urlpatterns=[
    path('',views.index,name='blog_main_view'),
    re_path(r'^$',views.index,name='blog_main_view'),
]