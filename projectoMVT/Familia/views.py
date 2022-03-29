from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def familia(request):

    plantilla = loader.get_template("familia.html")
    return HttpResponse(plantilla.render())