from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from datetime import datetime
from App1.forms import *


# Create your views here.
def inicio(request):
    return render(request, "App1/index.html")

def agregar(request):
    if request.method == "POST":
        miFormulario = AgregarFormulario(request.POST)
   
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cafeteria = Cafeterias(name=info['name'], direccion=info['direccion'], horario=info['horario'], descripcion=info['descripcion'] )
            cafeteria.save()
            
            return render(request, "App1/postAgregar.html")
    else:
        miFormulario = AgregarFormulario()
    
        
    return render(request, "App1/agregar.html", {"miFormulario": miFormulario})
     
def suscribirse(request):
    if request.method == "POST":
        userFormulario = SuscribirseFormulario(request.POST)
   
        if userFormulario.is_valid():
            info_ = userFormulario.cleaned_data
            usuario = Suscriptos(username=info_['username'], email=info_['email'], password=info_['password'], first_name=info_['first_name'], last_name=info_['last_name'] )
            usuario.save()
            
            return render(request, "App1/postSuscripcion.html")
    else:
        userFormulario = SuscribirseFormulario()
  
    return render(request, "App1/suscribirse.html",{"userFormulario": userFormulario})

def valoranos(request):
    if request.method == "POST":
       reseñaFormulario = ReseñaFormulario(request.POST)
   
       if reseñaFormulario.is_valid():
            info_ =reseñaFormulario.cleaned_data
            usuario = Reseñas(name=info_['name'], opinion=info_['opinion'], puntaje=info_['puntaje'])
            usuario.save()
            
            return render(request, "App1/postValoracion.html")
    else:
       reseñaFormulario = ReseñaFormulario()
  
    return render(request, "App1/valoranos.html",{"reseñaFormulario":reseñaFormulario})
 


def leerCafeterias(request):

      cafeterias = Cafeterias.objects.all() 

      contexto= {"cafeterias":cafeterias} 

      return render(request, "App1/cafeterias.html",contexto)
  
  


  
def buscarCafeterias(request):
    if request.method =="POST":
        buscarFormulario = BuscarCafeterias(request.POST)
        if buscarFormulario.is_valid():
           info = buscarFormulario.cleaned_data
           cafeterias = Cafeterias.objects.filter(direccion__icontains=info["direccion"])
           return render(request, "App1/mostrarBusqueda.html", {"cafeterias": cafeterias})
    else:
        buscarFormulario=BuscarCafeterias()
        
       
    return render(request, "App1/buscarCafeterias.html", {"buscarFormulario":buscarFormulario})

