from django.shortcuts import render
import random
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
from django.contrib.auth.decorators import login_required
import random
orden = 0
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

@login_required
def FinalizarCompra(request):
    total = str(Carrito.objects.all().aggregate(Sum(F('precio'))))
    total_carrito = re.findall("\d+\.\d+",total)
    entrega = datetime.now()+timedelta(days=4)
    productoslistados = Carrito.objects.all()
    if request.method == 'POST':
        cliente = request.POST['cliente']
        cliente2 = request.POST['cliente2']
        nit = request.POST['nit']
        direccion = request.POST['direccion']
        forma_pago = request.POST['pago']
        numorden = int(random.random()*1000)
        venta = Venta.objects.create(usuario_venta_id=cliente2,cliente=cliente, nit=nit, direccion=direccion, forma_pago=forma_pago, total=total_carrito[0], entrega=entrega, numorden = numorden)
        venta.save();
        productoslistados=Carrito.objects.all().delete()
        context = {}
        print("Usuario registrado")
        messages.info(request, 'La orden fue realizada exitosamente.')
        return render(request, 'venta/finalorden.html', context)
    else:
        return render(request, "venta/finalorden.html", {"total_carrito":total_carrito[0], "carrito": productoslistados, "entrega": entrega})

@login_required
def Order(request):
    categorys = Category.objects.all()
    detalles = Venta.objects.all()
    productoslistados = Carrito.objects.all()
    nombres = Usuario.objects.all()
    context = {'detalles': detalles, 'productoslistados': productoslistados, 'nombres': nombres,'categorys': categorys}
    return render(request, 'interface/ordenes.html', context)


def details(request, id,username,numorden):
    categorys = Category.objects.all()
    detalles = Venta.objects.all()
    productoslistados = Carrito.objects.all()
    productos= Product.objects.get(id=id)
    cliente = Usuario.objects.get(username=username)
    numorden = Venta.objects.get(numorden=numorden)
    #direccion = Venta.objects.get(direccion=direccion)
    compra = Ordenes.objects.create(cliente=cliente.username, producto = productos.name, numorden = numorden.numorden)
    compra.save();
    print("Usuario registrado")
    return redirect('/detalle')

def detal_order(request):
    
    return render(request, 'interface/detalle.html')

def deteccion(request, id):
    #usuarios= Usuario.objects.get(id=id)
    #compra = Ordenes.objects.create(usuario = usuarios.name, usuario_id = usuarios.id)
    #compra.save();
    #print("Usuario registrado")
    return redirect('/account')

def deteccion(request, id):
    record = Usuario.objects.get(id=id)
    context = {
        'record' : record
    }
    return render(request, 'interface/details.html', context)