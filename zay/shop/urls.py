from django.urls import path
from django.urls import path, include
from .views import IndexView, AboutTemplateView, CatalogListView, CategoryListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('shop/', CatalogListView.as_view(), name='shop'),
    path('shop/<slug:category_slug>', CategoryListView.as_view(), name='category'),
    path('shop/', include('api.catalog.urls')),
]
