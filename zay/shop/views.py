from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from .forms import ContactForm
from .models import Category, Product, Brand, SubCategory


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        categories = Category.objects.all().order_by('name')
        products = Product.objects.filter(is_published=1).order_by('title')
        context.update({
            'categories': categories,
            'products': products,
            'contact_form': ContactForm(),
            'contact_error': None
        })
        return context

    def post(self, request):
        content = self.get_context_data()
        form = ContactForm(request.POST)
        content['contact_error'] = None
        if form.is_valid():
            form.save()
        else:
            content['contact_error'] = 'Error'
        return self.get(request=request)


class AboutTemplateView(TemplateView):
    template_name = 'shop/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context['brands'] = Brand.objects.all().order_by('name')
        return context


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
    template_name = 'shop/shop.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True).order_by('id')

    def get_context_data(self):
        context = super(CatalogListView, self).get_context_data()
        context.update(self.context)
        categories = Category.objects.all()
        subcategories = SubCategory.objects.filter(is_published=True)
        context.update({
            'categories': categories,
            'subcategories': subcategories,
        })
        return context


class CategoryListView(ShopMixin, TemplateView):
    template_name = 'shop/shop.html'

    def get_queryset(self, slug):
        return Product.objects.filter(category__slug=slug)

    def get_context_data(self):
        context = super(CategoryListView, self).get_context_data()
        context.update(self.context)
        categories = Category.objects.all()
        subcategories = SubCategory.objects.filter(is_published=True)
        context.update({
            'categories': categories,
            'subcategories': subcategories,
        })
        return context

    def get(self, request, category_slug):
        return render(request, self.template_name, self.get_context_data() | {'products': self.get_queryset(category_slug)})


def error404(request, exception):
    return HttpResponse('<b>404<b>')
