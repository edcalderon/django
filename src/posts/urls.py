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

urlpatterns = [
    path('', post_list),
    path('create/', post_create),
    url(r'detail/(?P<id>\d+)/$', post_detail),
    path('update/', post_update),
    path('delete/', post_delete),
]