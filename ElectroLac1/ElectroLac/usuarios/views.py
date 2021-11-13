from django.shortcuts import render, redirect
from usuarios.forms import UsuariosForm
from usuarios.models import Usuario
from django.contrib import messages
from usuarios.models import Usuario
from venta.models import  *

# Create your views here.

def registroadmin(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        edad = request.POST['edad']
        photo = request.POST.get('photo')
        password = request.POST['password']
        type = request.POST['type']
        form = UsuariosForm(request.POST, request.FILES)
        if form.is_valid():
                photo = form.cleaned_data.get("photo")

        if Usuario.objects.filter(username=username).exists():
            messages.info(request, 'El nombre de usuario "Username" ya existe')
            return redirect('/account')
        elif Usuario.objects.filter(email=email).exists():
            messages.info(request, 'El correo "Email" ya fue registrado anteriormente')
            return redirect('/account')
        else:
            user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, edad=edad, type=type, photo=photo)
            user.save();
            messages.info(request, 'El nuevo usuario ha sido registrado exitosamente')
            print("Usuario registrado")
            return redirect('/account')
        


    else:
        context['form'] = UsuariosForm()
        return render(request, "usuarios/registrar.html", context)

def form_photo(request):
    context = {}
    context['form'] = UsuariosForm()
    return render(request, "usuarios/registrar.html", context)


#def login_foto(request, id,username,numorden):
#    categorys = Category.objects.all()
#    detalles = Venta.objects.all()
#    productoslistados = Carrito.objects.all()
#    productos= Product.objects.get(id=id) 
#    usuario = Usuario.objects.get(username=username)
#    numorden = Venta.objects.get(numorden=numorden)
#    #direccion = Venta.objects.get(direccion=direccion)
#    compra = Ordenes.objects.create(cliente=cliente.username, producto = productos.name, numorden = numorden.numorden)
#    compra.save();
#    print("Usuario registrado")
#    return redirect('/detalle')