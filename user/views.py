from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import RopaTrabajo
from .forms import RopaTrabajoFormulario, BusquedaRopaTrabajo

from .models import Toldos
from .forms import ToldosFormulario

from .models import ArtCamping
from .forms import ArtCampingFormulario

# * Ejemplo de CARGA DE TEMPLATE MANUAL
def inicio(request):
    template = loader.get_template("user/inicio.html")
    return HttpResponse(template.render())


def probando_template(request):
    contexto = {
        "nom": "Juan",
        "ap": "Perez",
        "notas": [10, 7, 3, 9],
    }
    return render(request, "user/probando.html", contexto)


def ropaTrabajo(request):
    ropaTrabajo= RopaTrabajo.objects.all()
    contexto = {"ropaTrabajo":ropaTrabajo}    
    return render(request, "user/RopaTrabajo.html", contexto)

def toldo(request):
    toldos= Toldos.objects.all()
    contexto = {"toldos":toldos}    
    return render(request, "user/Toldos.html", contexto)

def artc(request):
    articulo= ArtCamping.objects.all()
    contexto = {"articulo":articulo}    
    return render(request, "user/ArtCamping.html", contexto)



def ropaTrabajoFormulario(request):
    if request.method == "POST":
        form = RopaTrabajoFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            talle = form.cleaned_data["talle"]
            precio = form.cleaned_data["precio"]

            ropa = RopaTrabajo(nombre=nombre, talle=talle,precio=precio)
            ropa.save()
            return render(request, "user/RopaTrabajo_exito.html")
    else:
        form = RopaTrabajoFormulario()
    return render(request, "user/RopaTrabajo_formulario.html", {"form": form})

def toldoFormulario(request):
    if request.method == "POST":
        form = ToldosFormulario(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data["cliente"]
            tipo_toldo = form.cleaned_data["tipo_toldo"]
            precio = form.cleaned_data["precio"]

            told = Toldos(cliente=cliente, tipo_toldo=tipo_toldo,precio=precio)
            told.save()
            return render(request, "user/Toldos_exito.html")
    else:
        form = ToldosFormulario()
    return render(request, "user/Toldos_formulario.html", {"form": form})

def artcFormulario(request):
    if request.method == "POST":
        form = ArtCampingFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            precio = form.cleaned_data["precio"]

            art = ArtCamping(nombre=nombre, precio=precio)
            art.save()
            return render(request, "user/ArtCamping_exito.html")
    else:
        form = ArtCampingFormulario()
    return render(request, "user/ArtCamping_formulario.html", {"form": form})


def buscarRopaTrabajo(request):
    if request.method == "GET":
        form = BusquedaRopaTrabajo(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            resultados = RopaTrabajo.objects.filter(nombre=nombre)
            return render(
                request,
                "user/resultados_busqueda.html",
                {"resultados": resultados, "form": form},
            )
    else:
        form = BusquedaRopaTrabajo()
    return render(request, "user/buscar_RopaTrabajo.html", {"form": form})

