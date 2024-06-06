from django.shortcuts import render
from .models import Recetas
from .models import Comentario
from .models import Contacto

def Inicio (req):
    return render(req, 'inicio.html', {})

def crear_receta(req):

    if req.method == 'POST':

        nueva_receta = Recetas(nombre=req.POST['nombre'], ingredientes=req.POST['ingredientes'])
        nueva_receta.save()
        return render(req, 'inicio.html', {})

    else:

     return render(req, 'nueva_receta.html')

def lista_recetas(req):
    lista = Recetas.objects.all()
    return render(req, "lista_recetas.html", {"lista_recetas" : lista})

def comentario(req):
    if req.method == 'POST':
        
        nuevo_comentario = Comentario(nombre_de_usuario=req.POST['nombre_de_usuario'], apellido_de_usuario=req.POST['apellido_de_usuario'], comentario=req.POST['comentario'])
        nuevo_comentario.save()
    return render(req, 'comentario.html', {})

def contacto(req):

    if req.method == 'POST':

        nuevo_contacto = Contacto(nombre=req.POST['nombre'], email=req.POST['email'], 
                                  telefono=req.POST['telefono'],mensaje=req.POST['mensaje'])
        nuevo_contacto.save()
        return render(req, 'contacto.html', {"tu mensaje se ha enviado con éxito"})

    else:

        return render(req, 'contacto.html', {})

