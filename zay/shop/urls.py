from django.urls import path, register_converter, re_path

from .views import index
from django.conf.urls import handler404


urlpatterns = [
    path('', index),
]
