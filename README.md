# projectoMVT
Mi primer MVT

En la rama principal desarrolle toda la base hasta que llegue a la parte de la visualizacion de los familiares. Como no sabia como hacerlo, cree una rama por las dudas que empiece a fallar todo. Al terminar la visualizacion uni la rama secundaria a la principal.

Con la url "http://127.0.0.1:8000/familia/" --> accedes a la carga de los familaires.

Con la url "http://127.0.0.1:8000/familia/agregar-familiar/nombre/apellido/num_de_la_suerte/nacimiento --> creas nuevos familiares.
  
Para poder acceder a la base de datos utilice la siguiente funcion:
  
  def mostrar_familia(request):
  
    familia = Familia.objects.all()
    return render(request, "familia.html", {"familia": familia})
  
