"""proyectoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('', views.home , name="home"),
    path('about-me/', views.about , name="about-me"),
    path('contact/', views.contact , name="contacto"),
    path('index/', views.index , name="presenta"),
    path('imagen_movimiento/', views.imagen_movimiento , name="imagen"),
    path('contacto_2/', views.contacto_2 , name="New_contacto"),
    path('nueva_pantalla/', views.nueva_pantalla , name="New_pantalla"),
    path('contact_3/', views.contact_3, name="Contacto3"),
    path('about_2/', views.about_2, name="new_about"),
    path('portfolio/', views.portfolio, name="portafolio"),
    path('actualizar_docente/', views.actualizar_docente, name="actualizar"),
    path('consultar_docente/', views.consultar_docente, name="consultar"),
    path('crear_docente/', views.creardocente.as_view(), name="crear"),
    path('eliminar_docente/', views.eliminar_docente, name="eliminar"),
    path('admin/', admin.site.urls),
]
