# Generated by Django 3.2.9 on 2021-11-12 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0014_remove_ordenes_direccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenes',
            name='entrega',
        ),
        migrations.RemoveField(
            model_name='ordenes',
            name='forma_pago',
        ),
    ]
