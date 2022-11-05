from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .forms import ContactForm
from .models import Category, Product, Brand


class IndexView(View):
    template_name = 'shop/index.html'

    def get_context_data(self):
        categories = Category.objects.all().order_by('name')
        products = Product.objects.filter(is_published=1).order_by('title')
        content = {
            'categories': categories,
            'products': products,
            'contact_form': ContactForm,
            'contact_error': None
        }
        return content

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        content = self.get_context_data()
        form = ContactForm(request.POST)
        content['contact_error'] = None
        if form.is_valid():
            form.save()
        else:
            content['contact_error'] = 'Error'
        return render(request, self.template_name, content)

def about(request: HttpRequest):
    brands = Brand.objects.all().order_by('name')

    return render(
        request,
        'shop/about.html',
        {'brands': brands}
        )

class ContextMixin:
    context = {
        'site_title': 'Zay',
        'nav_home': 'Home',
        'nav_about': 'About',
        'nav_shop': 'Shop',
        'nav_contact': 'Contact',
        'shop_address': 'Svobody Street, 4, Minsk',
        'shop_email': 'info@zay.com',
        'shop_phone': '+375(33)-34-34-612',
        'facebook': 'https://facebook.com',
        'instagram': 'https://www.instagram.com/',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://www.linkedin.com/',
        'designed_by': 'https://templatemo.com/',
    }
class ShopMixin(ContextMixin):
    context = ContextMixin.context
    context.update({
        'name': 'Categories',
    })


class CatalogListView(ShopMixin, ListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self):
        context = super(CatalogListView, self).get_context_data()
        context.update(self.context)
        categories = Category.objects.all()
        context.update({
            'categories': categories,
            # 'subcategories': subcategories,
        })
        return context

def error404(request, exception):
    return HttpResponse('<b>404<b>')
