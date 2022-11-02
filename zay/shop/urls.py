from django.urls import path, register_converter, re_path

from .views import IndexView, about
from django.conf.urls import handler404


urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', about, name='about'),
]
