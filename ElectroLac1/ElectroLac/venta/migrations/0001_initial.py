# Generated by Django 3.2.9 on 2021-11-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Nombre')),
                ('slug', models.SlugField(editable=False)),
                ('summary', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('views', models.PositiveIntegerField(default=0)),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('Amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de venta')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='venta.category')),
            ],
        ),
    ]