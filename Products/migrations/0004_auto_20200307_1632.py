# Generated by Django 3.0.3 on 2020-03-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_auto_20200307_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Liquido', 'Liquido'), ('Polvo', 'Polvo')], max_length=100, verbose_name='Nombre'),
        ),
    ]
