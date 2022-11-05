import contacts as contacts
from django.urls import path, register_converter, re_path

from .views import IndexView, about, CatalogListView
from django.conf.urls import handler404


urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', about, name='about'),
    path('shop', CatalogListView.as_view(), name='shop'),
]
