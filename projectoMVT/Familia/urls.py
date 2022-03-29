from django.urls import path
from Familia import views

urlpatterns = [
    path("", views.familia),
    path("agregar-familiar/<nombre>/<apellido>/<num_de_la_suerte>/<nacimiento>", views.agregarFamiliar)
]