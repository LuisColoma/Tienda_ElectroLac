# Generated by Django 3.2.9 on 2021-11-11 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0007_order_orderline'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='venta.order'),
            preserve_default=False,
        ),
    ]