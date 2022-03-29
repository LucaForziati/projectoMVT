from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader

from Familia.models import Familia

# Create your views here.

def familia(request):

    plantilla = loader.get_template("familia.html")
    return HttpResponse(plantilla.render())

def agregarFamiliar(request, nombre, apellido, num_de_la_suerte, nacimiento):

    familiar_nuevo = Familia(
        nombre = nombre, 
        apellido = apellido,
        num_de_la_suerte = num_de_la_suerte,
        nacimiento = nacimiento
        )
    familiar_nuevo.save()

    plantilla = loader.get_template("agregarFamiliar.html")
    return HttpResponse(plantilla.render({
        "nombre": familiar_nuevo.nombre, 
        "apellido": familiar_nuevo.apellido, 
        "num_de_la_suerte": familiar_nuevo.num_de_la_suerte, 
        "nacimiento": familiar_nuevo.nacimiento
        }))