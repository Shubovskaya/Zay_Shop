from django.contrib import admin
from .models import Category, SubCategory, Product, Brand, Order, OrderItem, Basket


class ProductTabularInline(admin.TabularInline):
    model = Product


class SubCategoryTabularInline(admin.TabularInline):
    model = SubCategory
    can_delete = False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    # actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя категории или id категории'
    inlines = (SubCategoryTabularInline,)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    # actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя категории или id категории'
    inlines = (ProductTabularInline,)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'is_published')
    list_filter = ('name', 'is_published')
    list_max_show_all = 5
    inlines = (ProductTabularInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    # actions = (make_published, make_unpublished)
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'Введите имя товара, id, артикул, цену'
    fieldsets = (
        ('Основные натройки', {
            'fields': ('title', 'article', 'price', 'category', 'sub_category', 'brand',),
            'description': 'описание'
        }),
        ('Дополнительные настройки', {
            'fields': ('is_published', 'descr', 'count')
        })
    )
    list_editable = ('category',)
    prepopulated_fields = {'descr': ('title', 'article')}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('user', 'date_created')
    list_filter = ('user', 'date_created')
    list_max_show_all = 10


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('order',)
    list_filter = ('order', 'product')
    list_max_show_all = 10


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'id',
        'customer',
        'created_date',
        'updated_date',
    )
    list_filter = ('created_date', 'created_date',)
    search_fields = ('id',)
    search_help_text = 'Enter id for search'
    readonly_fields = ('created_date', 'updated_date')
