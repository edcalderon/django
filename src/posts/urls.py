from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# imported views
from .views import (
        post_list,
        post_create,
        post_detail,
        post_update,
        post_delete,
    )

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create),
    url(r'(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'(?P<id>\d+)/delete/$', post_delete),
]

