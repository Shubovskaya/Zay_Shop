
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Category, Product, Brand
from django.shortcuts import render, get_object_or_404


def error404(request, exception):
    return HttpResponse('<b>404</b>')


def index(request: HttpRequest):
    error = None
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Ошибка'
    form = NewsLetterForm()
    return render(request,
                  'shop/index.html',
                  {
                      'news_letter_form': form,
                      'news_letter_error': error
                  })



def about(request: HttpRequest):
    brands = Brand.objects.all().order_by('name')

    return render(request,
                  'shop/about_us.html',
                  {'brands': brands}
                  )