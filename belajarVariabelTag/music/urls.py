from django.urls import path,re_path,include
from . import views
urlpatterns=[
    path('',views.index,name='home_main_view'),
]