from django import forms



# Formulario para agregar un nuevo curso
class RopaTrabajoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del artículo")
    talle = forms.CharField(max_length=50, label="Talle")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")

# Formulario para agregar un nuevo curso
class ToldosFormulario(forms.Form):
    cliente = forms.CharField(max_length=50,label="Nombre del cliente")
    tipo_toldo = forms.CharField(max_length=50, label="Tipo de Toldo")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")

class ArtCampingFormulario(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del artículo")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")

# Formulario de búsqueda de cursos por camada
class BusquedaRopaTrabajo(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del artículo")