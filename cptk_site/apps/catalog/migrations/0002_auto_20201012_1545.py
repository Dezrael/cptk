# Generated by Django 2.2.15 on 2020-10-12 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'verbose_name': '(4) Атрибут', 'verbose_name_plural': '(4) Атрибуты'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '(2) Категория', 'verbose_name_plural': '(2) Категории'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': '(3) Производитель', 'verbose_name_plural': '(3) Производители'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': '(5) Заказ', 'verbose_name_plural': '(5) Заказы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '(1) Товар', 'verbose_name_plural': '(1) Товары'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Категория родитель:'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=90, unique=True, verbose_name='URL:'),
        ),
        migrations.AlterField(
            model_name='category',
            name='svg',
            field=models.CharField(blank=True, max_length=30, verbose_name='Название SVG, для меню'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=90, unique=True, verbose_name='Наименование:'),
        ),
    ]
