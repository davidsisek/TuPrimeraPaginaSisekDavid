from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("probando/", views.probando_template, name="probando"),
    path("RopaTrabajo/", views.ropaTrabajo, name="RopaTrabajo"),
    path("RopaTrabajoFormulario/",views.ropaTrabajoFormulario, name="RopaTrabajoFormulario"),
    path("Toldos/", views.toldo, name="Toldos"),
    path("ToldosFormulario/",views.toldoFormulario, name="ToldosFormulario"),
    path("ArtCamping/", views.artc, name="ArtCamping"),
    path("ArtCampingFormulario/",views.artcFormulario, name="ArtCampingFormulario"),
    path("BuscarRopaTrabajo/",views.buscarRopaTrabajo, name="buscarRopaTrabajo"),
    
]