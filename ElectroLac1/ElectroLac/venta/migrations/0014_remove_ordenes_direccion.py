# Generated by Django 3.2.9 on 2021-11-12 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0013_remove_ordenes_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenes',
            name='direccion',
        ),
    ]