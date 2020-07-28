from django.shortcuts import render,HttpResponse

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
def home(request, plantilla="home.html"):
    return render(request, plantilla);
def about(request, plantilla="about.html"):
    return render(request, plantilla);
def contact(request, plantilla="contact.html"):
    return render(request, plantilla);
# Create your views here.
