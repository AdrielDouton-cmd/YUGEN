from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Evento
from .forms import ClienteForm, EventoForm, ReservaForm


# REGISTRO DE CLIENTES Y BUSQUEDA EN BD
def crear_registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'registrarse.html', {'form': form})

def busqueda_cliente(request):
    return render(request, "busquedaCliente.html")

def buscar_cliente(request):
    
    var_nombre = request.GET.get("nombre", "").strip()
    clientes = Cliente.objects.filter(nombre=var_nombre)

    return render(request, "resultado_busqueda_cliente.html", { "clientes" : clientes, "nombre_del_cliente" : var_nombre})


# REGISTRO DE EVENTOS Y BUSQUEDA EN BD
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventoForm()
    return render(request, 'eventos.html', {'form': form})

def busqueda_evento(request):
    return render(request, "busquedaEvento.html")

def buscar_evento(request):
    
    var_numero = request.GET.get("numero", "").strip()
    var_numero = int(var_numero)
    eventos = Evento.objects.filter(numero=var_numero)

    return render(request, "resultado_busqueda.html", { "eventos" : eventos, "numero_de_evento" : var_numero})


#REGISTRO DE RESERVAS
def reserva(req):
    return render(req, "reserva.html", {})

def hacer_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservaForm()
        return render(request, 'reserva.html', {'form': form})


#OTRAS PAGINAS
def inicio(req):
    return render(req, "inicio.html", {})
def carta(req):
    return render(req, "carta.html", {})
def locales(req):
    return render(req, "locales.html", {})


