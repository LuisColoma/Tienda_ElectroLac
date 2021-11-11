from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from usuarios.models import Usuario
from venta.models import  *
from venta.forms import ProductoForm, CarritoForm
from django.views.generic import ListView
from datetime import datetime, timedelta
from django.db.models import Sum, F
import re
# Create your views here.
def agregar_carrito(request, id, username):
    productos= Product.objects.get(id=id)
    cliente = Usuario.objects.get(username=username)
    compra = Carrito.objects.create(cliente=cliente.username, photo = productos.image, producto = productos.name, precio=productos.Amount)
    compra.save();
    print("Usuario registrado")
    return redirect('/account')

def Listarcarrito(request):
    if Carrito.objects.all().count() != 0:
        total = str(Carrito.objects.all().aggregate(Sum(F('precio'))))
        total_carrito = re.findall("\d+\.\d+",total)
        tot = total_carrito[0]
    else:
        tot = format(0.00, '.2f')
    productoslistados = Carrito.objects.all() 
    return render(request, "interface/carrito.html", {"total_carrito": tot, "carrito": productoslistados})

def Listarcarrito1(request):
    if Carrito.objects.all().count() != 0:
        total = str(Carrito.objects.all().aggregate(Sum(F('precio'))))
        total_carrito = re.findall("\d+\.\d+",total)
        tot = total_carrito[0]
    else:
        tot = format(0.00, '.2f')
    productoslistados = Carrito.objects.all() 
    return render(request, "interface/carrito1.html", {"total_carrito": tot, "carrito": productoslistados})

def eliminar_carrito(request,id):
    productoslistados= Carrito.objects.get(id=id)
    productoslistados.delete()

    return redirect('/carrito1')

def FinalizarCompra(request):
    total = str(Carrito.objects.all().aggregate(Sum(F('precio'))))
    total_carrito = re.findall("\d+\.\d+",total)
    entrega = datetime.now()+timedelta(days=3)
    productoslistados = Carrito.objects.all()
    if request.method == 'POST':
        cliente = request.POST['cliente']
        nit = request.POST['nit']
        direccion = request.POST['direccion']
        forma_pago = request.POST['pago']
        venta = Venta.objects.create(cliente=cliente, nit=nit, direccion=direccion, forma_pago=forma_pago, total=total_carrito[0], entrega=entrega)
        venta.save();
        productoslistados=Carrito.objects.all().delete()
        context = {}
        print("Usuario registrado")
        messages.info(request, 'La orden fue realizada exitosamente.')
        return render(request, 'venta/finalorden.html', context)
    else:
        return render(request, "venta/finalorden.html", {"total_carrito":total_carrito[0], "carrito": productoslistados, "entrega": entrega})

class OrderList(ListView):
    model = Venta
    ordering = ["-id"]
    template_name = "orders/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


