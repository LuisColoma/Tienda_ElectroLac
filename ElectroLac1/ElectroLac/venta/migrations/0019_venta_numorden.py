# Generated by Django 3.2.9 on 2021-11-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0018_remove_venta_numorden'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='numorden',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
