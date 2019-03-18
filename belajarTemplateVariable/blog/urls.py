from django.urls import path,re_path
from . import views
urlpatterns=[
    re_path(r'^$',views.index,name='blog_main_view'),
    re_path(r'^cerita/$',views.cerita,name='cerita_view'),
    re_path(r'^resep/$',views.resep,name='resep_view'),
]