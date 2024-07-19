from django.urls import path, include
from catalogos.views import *
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [

    #____ Home
    path('',home,name="home"),

    #____ Plantas
    path('nuestrasPlantas',nuestrasPlantas,name="nuestrasPlantas"),
    path('buscarPlantas/',buscarPlantas,name='buscarPlantas'),
    path('encontrarPlantas/',encontrarPlantas,name="encontrarPlantas"),

    #____ Jardines
    path('jardines',jardines,name="jardines"),
    path('buscarJardines/',buscarJardines,name='buscarJardines'),
    path('encontrarJardines/',encontrarJardines,name="encontrarJardines"),

    #____ Cultivos
    path('cultivando',cultivando,name="cultivando"),
    path('buscarCultivos/',buscarCultivos,name='buscarCultivos'),
    path('encontrarCultivos/',encontrarCultivos,name="encontrarCultivos"),
    path('rosales/',rosales,name="rosales"),
    path('lavanda/',lavanda,name="lavanda"),

    #____ Contactos y comentarios
    path('contacto',contacto,name="contacto"),
    path('contactoRealizado',contacto,name="contactoRealizado"),
    path('contactoComentarios',comentarios,name="comentarios"),
    path('contactoUpdate/<id_contacto>/',contactoUpdate,name="contactoUpdate"),
    path('contactoDelete/<id_contacto>/',contactoDelete,name="contactoDelete"),

    #____ Inicio sesión / Finalización sesión / Registración
    path('login/',loginRequest,name="login"),
    path ('logout/',LogoutView.as_view(template_name="catalogos/logout.html"),name="logout"),
    path('registro/',register,name="registro"),
    
    #____ Edición de Perfil / Avatar
    path ('perfil/',editProfile, name="perfil"),
    path ('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path ('agregar_avatar/',agregarAvatar, name="agregar_avatar"),

    #____ Acerca
    path ('acerca/', acerca, name='acerca'),
    
    #____ Mapa del sitio
    path ('mapaDelSitio/', mapaDelSitio, name='mapaDelSitio'),

    ]
