from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='название категории',
        help_text='Макс. 24 символа'
    )

    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='Макс. 36 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('is_published', 'name')


class SubCategory(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='название подкатегории',
        help_text='Макс. 24 символа'
    )
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='род. категория'
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='Макс. 140 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_sub_categories'
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
        ordering = ('is_published', 'name')


class Brand(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='бренд',
        help_text='Макс. 24 символа'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )


class Product(models.Model):
    title = models.CharField(
        max_length=56,
        verbose_name='название',
        help_text='Макс. 48 символов'
    )
    category = models.ForeignKey(
        'SubCategory',
        on_delete=models.PROTECT,
        verbose_name='подкатегория',
    )
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        verbose_name='бренд',
        help_text='Макс. 16 символов'
    )
    descr = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='описание',
        help_text='Макс. 56 символов'
    )
    article = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='артикул',
        help_text='Макс. 16 символов'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='публикация'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text='Макс. 999999.99'
    )
    count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='количество'
    )
    image = models.ImageField(
        upload_to='products',
        verbose_name='изображение',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price', 'title', 'article')


class Order(models.Model):
    title = models.CharField(
        max_length=45,
        verbose_name='заказ',
        help_text='Макс. 36 символов'
    )
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        on_delete=models.DO_NOTHING,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True
    )
    date_created = models.DateTimeField(
        default=now(),
        blank=True
    )
    is_paid = models.BooleanField(
        default=0,
        verbose_name='статус оплаты',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_orders'
        verbose_name = 'заявка/заказ'
        verbose_name_plural = 'заявки/заказы'
        ordering = ('product', 'user')


class OrderItem(models.Model):
    order = models.ForeignKey(
        'Order',
        verbose_name='заказ',
        on_delete=models.DO_NOTHING
    )
    product = models.ForeignKey(
        'Product',
        verbose_name='товары в заказе',
        on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table = 'shop_order_items'
        verbose_name = 'состав заказа'
        verbose_name_plural = 'состав заказов'
        ordering = ('order', 'product')


class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    message = models.CharField(max_length=1024)
    date_created = models.DateTimeField(default=datetime.utcnow(), verbose_name='дата публикации')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'shop_contacts'
        ordering = ('date_created',)
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'
