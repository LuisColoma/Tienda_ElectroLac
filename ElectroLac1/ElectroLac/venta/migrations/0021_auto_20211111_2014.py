# Generated by Django 3.2.9 on 2021-11-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0020_auto_20211111_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(default='', max_length=50)),
                ('producto', models.CharField(default='', max_length=50)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('total', models.PositiveIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('photo', models.ImageField(default='images/deafualt1.png', upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='ordenes',
            name='numorden',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
