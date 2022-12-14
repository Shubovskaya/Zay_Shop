# Generated by Django 4.1.2 on 2022-10-26 15:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Макс. 24 символа', max_length=24, verbose_name='бренд')),
                ('is_published', models.BooleanField(default=False, verbose_name='публикация')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Макс. 24 символа', max_length=24, verbose_name='название категории')),
                ('descr', models.CharField(blank=True, help_text='Макс. 36 символов', max_length=140, null=True, verbose_name='описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='публикация')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'shop_categories',
                'ordering': ('is_published', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=1024)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 10, 26, 15, 1, 10, 675573), verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'обращение',
                'verbose_name_plural': 'обращения',
                'db_table': 'shop_contacts',
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Макс. 36 символов', max_length=45, verbose_name='заказ')),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 26, 15, 1, 10, 674574, tzinfo=datetime.timezone.utc))),
                ('is_paid', models.BooleanField(default=0, verbose_name='статус оплаты')),
            ],
            options={
                'verbose_name': 'заявка/заказ',
                'verbose_name_plural': 'заявки/заказы',
                'db_table': 'shop_orders',
                'ordering': ('product', 'user'),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Макс. 24 символа', max_length=24, verbose_name='название подкатегории')),
                ('descr', models.CharField(blank=True, help_text='Макс. 140 символов', max_length=140, null=True, verbose_name='описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='публикация')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='род. категория')),
            ],
            options={
                'verbose_name': 'подкатегория',
                'verbose_name_plural': 'подкатегории',
                'db_table': 'shop_sub_categories',
                'ordering': ('is_published', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Макс. 48 символов', max_length=56, verbose_name='название')),
                ('descr', models.CharField(blank=True, help_text='Макс. 56 символов', max_length=255, null=True, verbose_name='описание')),
                ('article', models.CharField(help_text='Макс. 16 символов', max_length=16, unique=True, verbose_name='артикул')),
                ('is_published', models.BooleanField(default=False, verbose_name='публикация')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Макс. 999999.99', max_digits=8, verbose_name='цена')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='количество')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='изображение')),
                ('brand', models.ForeignKey(help_text='Макс. 16 символов', on_delete=django.db.models.deletion.CASCADE, to='shop.brand', verbose_name='бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.subcategory', verbose_name='подкатегория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'db_table': 'shop_products',
                'ordering': ('price', 'title', 'article'),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.order', verbose_name='заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.product', verbose_name='товары в заказе')),
            ],
            options={
                'verbose_name': 'состав заказа',
                'verbose_name_plural': 'состав заказов',
                'db_table': 'shop_order_items',
                'ordering': ('order', 'product'),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
