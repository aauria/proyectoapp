from django.shortcuts import render,HttpResponse,redirect
from .form import DocenteForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Docente

html_base="""
    <h1>Mi Primer Menu</h1>
    <ul>
        <li> <a href="/">Portada</a>    </li>
        <li> <a href="/about-me/">Acerca de</a>    </li>
    </ul>
"""

def home(request):
    html_responsde = "<h1>la pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);
def about(request):
    html_responsde = "<h1>Acerca De </h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);


def index(request, plantilla="index.html"):
    return render(request, plantilla);
def home(request, plantilla="home.html"):
       return render(request, plantilla);
def about(request, plantilla="about.html"):
    return render(request, plantilla);
def contact(request, plantilla="contact.html"):
    return render(request, plantilla);
def imagen_movimiento(request, plantilla="imagen_movimiento.html"):
    return render(request, plantilla);
def contacto_2(request, plantilla="contacto_2.html"):
    return render(request, plantilla);
def nueva_pantalla(request, plantilla="nueva_pantalla.html"):
    return render(request, plantilla);
def about_2(request, plantilla="about_2.html"):
    return render(request, plantilla);
def contact_3(request, plantilla="contact_3.html"):
    return render(request, plantilla);
def portfolio(request, plantilla="portfolio.html"):
    return render(request, plantilla);
#CRUD tabla docente
def crear_docente(request):
     if request.method == 'GET':
         form=DocenteForm()
         contexto={
            'form':form
         }
     else:
         form = DocenteForm(request.POST)
         contexto = {
             'form': form
         }
         if form.is_valid():
             form.save()
             return redirect ('New_pantalla')

     return render(request,'crear_docente.html',contexto)

class creardocente(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'consultar_docente.html'
    success_url = reverse_lazy('New_pantalla')

def actualizar_docente(request,plantilla='actualizar_docente'):
    return render(request,plantilla);
def eliminar_docente(request,plantilla='eliminar_docente'):
    return render(request,plantilla);
def consultar_docente(request,plantilla='consultar_docente'):
    return render(request,plantilla);
# Create your views here.
