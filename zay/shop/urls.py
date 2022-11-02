from django.urls import path, register_converter, re_path

from .views import index, about
from django.conf.urls import handler404


urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
]

handler404 = 'shop.views.error404'

