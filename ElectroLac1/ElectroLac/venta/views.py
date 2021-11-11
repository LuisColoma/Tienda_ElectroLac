from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from usuarios.models import Usuario
from venta.models import Producto, Carrito, Venta
from venta.forms import ProductoForm, CarritoForm
from django.views.generic import ListView
from datetime import datetime, timedelta
from django.db.models import Sum, F
import re
# Create your views here.
def agregar_carrito(request, id, username):
    productos= Producto.objects.get(id=id)
    cliente = Usuario.objects.get(username=username)
    compra = Carrito.objects.create(cliente=cliente.username, photo = productos.photo, producto = productos.nombre, precio=productos.precio)
    compra.save();
    print("Usuario registrado")
    return redirect('/carrito')