from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Category


def index(request):
    return render(request, 'shop/base.html')


def about(request):
    return render(request, 'shop/about.html')


