from django.shortcuts import render, redirect
from venta.models  import Product, Category
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from usuarios.models import Usuario

# Create your views here.
def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/home.html', context)

def account(request):
    categorys = Category.objects.all()
    products = Product.objects.all() 
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/account.html', context)

#def carrito(request):
    #carro = Carrito.objects.all()
    #context = {'carro': carro}
    #return render(request, 'interfaz/carrito.html')

def arduino(request):
    #categorys = Category.objects.all()
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/arduino.html', context)

def capacitores(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/capacitores.html', context)

def motores(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/motores.html', context)

def resistencias(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/resistencias.html', context)

def transistores(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'categorys': categorys}
    return render(request, 'interface/transistores.html', context)

def orders(request):
    return render(request, 'interface/transistores.html')

def perfil(request):
    categorys = Category.objects.all()
    informacion = Usuario.objects.all()
    context = {'informacion': informacion,'categorys': categorys}
    return render(request, 'interface/perfil.html', context)
