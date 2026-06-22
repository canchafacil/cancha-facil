from django.shortcuts import render, redirect
from django.contrib import messages

def inicio(request):
    """Renderiza la página de inicio."""
    return render(request, 'principal/index.html') 

def reservas(request):
    """Renderiza la sección principal de reservas."""
    return render(request, 'principal/reservas.html')

def canchas(request):
    """Renderiza el catálogo de canchas disponibles."""
    return render(request, 'principal/canchas.html')

def pago(request):
    """Renderiza el módulo de pago final."""
    return render(request, 'principal/pago.html')

def nosotros(request):
    """Renderiza la página Sobre Nosotros."""
    return render(request, 'principal/nosotros.html')

def contacto(request):
    """Renderiza la página de Contacto."""
    return render(request, 'principal/contacto.html')

def formulario(request):
    """Renderiza el archivo formulario.html secundario."""
    return render(request, 'principal/formulario.html')

def inicio_admi(request):
    """Renderiza el panel inicial de administración."""
    return render(request, 'principal/inicioadmi.html')

def admin_panel(request):
    return render(request, 'principal/admi.html')