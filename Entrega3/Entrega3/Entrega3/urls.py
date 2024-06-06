from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nueva_receta', views.crear_receta, name='nueva receta'),
    path('lista_recetas/', views.lista_recetas, name='lista_recetas'),
    path('comentario/', views.comentario, name='comentario'),
    path('contacto/', views.contacto, name='contacto'),
    path('', views.Inicio, name= 'inicio'),

]
