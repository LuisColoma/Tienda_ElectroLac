"""ElectroLac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from interface.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from usuarios.views import *
from interface.views import *
from venta.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name = 'home'),
    path('', account),
    path('login/', LoginView.as_view(template_name='interface/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='login.html'), name='logout'),
    path("account/", account, name="account"),
    path('registrar/', registroadmin, name='registrar'),
    path('home/Arduino.html', arduino, name='Arduino'),
    path('home/Resistencias.html', resistencias, name='Resistencias'),
    path('home/Capacitores.html', capacitores, name='Capacitores'),
    path('home/Transistores.html', transistores, name='Transistores'),
    path('home/Motores.html', motores, name='Motores'),
    path('account/Arduino.html', arduino, name='Arduino'),
    path('account/Resistencias.html', resistencias, name='Resistencias'),
    path('account/Capacitores.html', capacitores, name='Capacitores'),
    path('account/Transistores.html', transistores, name='Transistores'),
    path('account/Motores.html', motores, name='Motores'),
    path('home/carrito.html', Listarcarrito),
    path('me/carrito.html', Listarcarrito),
    path('carrito/', Listarcarrito),
    path('carrito1/', Listarcarrito1),
    path('account/carrito.html', Listarcarrito1, name='carrito1'),
    path('<slug:username>/producto/<int:id>', agregar_carrito),
    path('account/eliminacionProducto/<int:id>', eliminar_carrito),
    path('carrito1/eliminacionProducto/<int:id>', eliminar_carrito),
    path('checkout/', FinalizarCompra),
    path('me/', Order, name='order_list'),
    path('<slug:username>/details/<int:id>/<int:numorden>', details),
       path("detalle/", detal_order, name="detalle"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)