# Generated by Django 2.2.15 on 2020-10-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_productfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfiles',
            name='title',
            field=models.CharField(default=' ', max_length=120, verbose_name='Наименование'),
            preserve_default=False,
        ),
    ]
