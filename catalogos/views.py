from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

#____ Home
def home(request):
    return render(request,"catalogos/index.html")

#____ Plantas
def nuestrasPlantas(request):
    contexto = {"plantas": Plantas.objects.all()}
    return render(request,"catalogos/nuestrasPlantas.html", contexto)

def buscarPlantas(request):
    return render(request,'catalogos/buscarPlantas.html')

def encontrarPlantas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        plantas = Plantas.objects.filter(nombre__icontains=patron)
        contexto = {"plantas": plantas}
    else:
        contexto = {"plantas": Plantas.objects.all()}
    return render(request,"catalogos/nuestrasPlantas.html", contexto)

#____ Jardines
def jardines(request):
    contexto = {"jardines": Jardines.objects.all()}
    return render(request,"catalogos/jardines.html", contexto)

def buscarJardines(request):
    return render(request,'catalogos/buscarJardines.html')

def encontrarJardines(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        jardines = Jardines.objects.filter(nombre__icontains=patron)
        contexto = {"jardines": jardines}
    else:
        contexto = {"jardines": Jardines.objects.all()}
    return render(request,"catalogos/jardines.html", contexto)

#____ Cultivos
def cultivando(request):
    contexto = {"cultivando": Cultivos.objects.all()}
    return render(request,"catalogos/cultivando.html",contexto)

def buscarCultivos(request):
    return render(request,'catalogos/buscarCultivos.html')

def encontrarCultivos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cultivos = Cultivos.objects.filter(nombre__icontains=patron)
        contexto = {"cultivando": cultivos}
    else:
        contexto = {"cultivando": Jardines.objects.all()}
    return render(request,"catalogos/cultivando.html", contexto)

def rosales(request):
    reprRosales = Reproduccion.objects.filter(nombre__icontains="rosales")
    contexto = {"reprRosales": reprRosales}
    return render(request,"catalogos/reprRosales.html",contexto)

def lavanda(request):
    reprLavanda = Reproduccion.objects.filter(nombre__icontains="lavanda")
    contexto = {"reprLavanda": reprLavanda}
    return render(request,"catalogos/reprLavanda.html",contexto)

#____ Contactos y comentarios
@login_required
def contacto(request):
    if request.method=="POST":
        miForm = Contacto(request.POST)
        if miForm.is_valid():
            contacto_apellido = miForm.cleaned_data.get("apellido")
            contacto_ciudad = miForm.cleaned_data.get("ciudad")
            contacto_pais = miForm.cleaned_data.get("pais")
            contacto_correo = miForm.cleaned_data.get("correo")
            contacto_telefono = miForm.cleaned_data.get("telefono")
            contacto_mensaje = miForm.cleaned_data.get("mensaje")
            contactos = Contactos(apellido=contacto_apellido,
                                ciudad=contacto_ciudad,
                                pais=contacto_pais,
                                correo=contacto_correo,
                                telefono=contacto_telefono,
                                mensaje=contacto_mensaje)
            contactos.save()
            contexto = {"contactos":Contactos.objects.all()}
            return render(request,"catalogos/contactoRealizado.html",contexto)
    else:
        miForm = Contacto()
        return render(request,"catalogos/contacto.html",{"form":miForm})

@login_required    
def contactoUpdate(request,id_contacto):
    contacto = Contactos.objects.get(id=id_contacto)
    if request.method =="POST":
        miForm = Contacto(request.POST)
        if miForm.is_valid():
            contacto.apellido = miForm.cleaned_data.get("apellido")
            contacto.ciudad = miForm.cleaned_data.get("ciudad")
            contacto.pais = miForm.cleaned_data.get("pais")
            contacto.correo = miForm.cleaned_data.get("correo")
            contacto.telefono = miForm.cleaned_data.get("telefono")
            contacto.mensaje = miForm.cleaned_data.get("mensaje")
            contacto.save()
            contexto = {"contactos":Contactos.objects.all()}
            return render(request,"catalogos/contactoRealizado.html",contexto)
    else:
        miForm = Contacto(initial={"apellido":contacto.apellido,
                                    "ciudad":contacto.ciudad,
                                    "pais":contacto.pais,
                                    "correo": contacto.correo,
                                    "telefono":contacto.telefono,
                                    "mensaje":contacto.mensaje})
    return render(request,"catalogos/contacto.html",{"form":miForm})

@login_required
def comentarios(request):
    contexto = {"contactos":Contactos.objects.all()}
    return render(request,"catalogos/contactoRealizado.html",contexto)

@login_required
def contactoDelete(request,id_contacto):
    contacto = Contactos.objects.get(id=id_contacto)
    contacto.delete()
    contexto = {"contactos":Contactos.objects.all()}
    return render(request,"catalogos/contactoRealizado.html",contexto)

#____ Inicio sesión / Finalización sesión / Registración
def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #____ Buscar Avatar
            try:
                avatar=Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request,"catalogos/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    return render(request, "catalogos/login.html",{"form":miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    return render(request,"catalogos/registro.html",{"form":miForm})

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request,"catalogos/editarperfil.html", {"form":miForm})
            
class CambiarClave (LoginRequiredMixin, PasswordChangeView):
    template_name = "catalogos/cambiar_clave.html"
    success_url = reverse_lazy("home")

#____ Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm (request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #____ Borra avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo)>0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            #____ Enviar la imagen añ home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request,"catalogos/agregarAvatar.html", {"form": miForm})

#____  Acerca
def acerca(request):
    return render (request, 'catalogos/acerca.html')

#____ Mapa del sitio
def mapaDelSitio(request):
    return render (request, 'catalogos/mapaDelSitio.html')
