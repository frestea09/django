from django.urls import path,re_path
from . import views
urlpatterns=[
    re_path(r'^$',views.index,name='about_main_view'),
    re_path(r'^ilman/$',views.autorSatu,name='ilman_author_view'),
    re_path(r'^lies/$',views.authorDua,name='lies_author_view'),
]