# Generated by Django 3.0.3 on 2020-03-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0012_auto_20200307_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
