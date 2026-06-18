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

def login_view(request):
    """Renderiza la pantalla de inicio de sesión."""
    return render(request, 'principal/login.html')

def registro(request):
    """Renderiza el formulario de registro y procesa los datos."""
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'principal/registro.html')
        
        messages.success(request, "¡Registro exitoso! Ya puedes iniciar sesión.")
        return redirect('login')

    return render(request, 'principal/registro.html')

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