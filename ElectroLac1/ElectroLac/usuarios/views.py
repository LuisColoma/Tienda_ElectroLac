from django.shortcuts import render, redirect
from usuarios.forms import UsuariosForm
from usuarios.models import Usuario
from django.contrib import messages

# Create your views here.

def registroadmin(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        edad = request.POST['edad']
        #photo = request.POST['photo']
        password = request.POST['password']
        type = request.POST['type']
        form = UsuariosForm(request.POST, request.FILES)
        #if form.is_valid():
                #photo = form.cleaned_data.get("photo")

        if Usuario.objects.filter(username=username).exists():
            messages.info(request, 'El nombre de usuario "Username" ya existe')
            return redirect('/account')
        elif Usuario.objects.filter(email=email).exists():
            messages.info(request, 'El correo "Email" ya fue registrado anteriormente')
            return redirect('/account')
        else:
            user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, edad=edad, type=type)
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