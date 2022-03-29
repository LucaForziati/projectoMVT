from django.urls import path
from Familia import views

urlpatterns = [
    path("", views.familia)
]