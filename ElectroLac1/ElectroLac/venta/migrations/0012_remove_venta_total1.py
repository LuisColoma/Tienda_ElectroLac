# Generated by Django 3.2.9 on 2021-11-12 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0011_alter_venta_total1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total1',
        ),
    ]
