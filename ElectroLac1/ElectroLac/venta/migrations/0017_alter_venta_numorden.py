# Generated by Django 3.2.9 on 2021-11-12 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0016_venta_numorden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='numorden',
            field=models.IntegerField(),
        ),
    ]