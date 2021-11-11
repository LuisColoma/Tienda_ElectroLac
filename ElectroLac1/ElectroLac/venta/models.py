from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Nombre', unique=True)
    slug = models.SlugField(editable=False)
    summary = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='productos', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    stock = models.IntegerField(default=0, verbose_name='Stock')
    Amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')


    def __str__(self):
        return self.name
    
    @property
    def get_photo_url(self):
        if self.image  and hasattr(self.image , 'url'):
            return self.image.url
        else:
            return "/static/img/not_available.png"


class Carrito(models.Model):
    cliente = models.CharField(max_length=50, default="")
    producto = models.CharField(max_length=50, default="")
    cantidad = models.PositiveIntegerField(default = 1)
    total = models.PositiveIntegerField(default = 1)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    photo = models.ImageField(default='images/deafualt1.png')

    def __str__(self):
        return f'{self.cliente}'