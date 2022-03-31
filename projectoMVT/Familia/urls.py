from django.urls import path
from Familia import views

urlpatterns = [
    path("", views.mostrar_familia),
    path("agregar-familiar/<nombre>/<apellido>/<num_de_la_suerte>/<nacimiento>", views.agregarFamiliar)
]