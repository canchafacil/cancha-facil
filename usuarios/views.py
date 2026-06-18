from django.shortcuts import render, redirect
from .models import Usuario

def registro(request):

    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(
                request,
                'usuarios/registro_admin.html',
                {'error': 'Las contraseñas no coinciden'}
            )

        if Usuario.objects.filter(email=email).exists():
            return render(
            request,
            'usuarios/registro_admin.html',
            {'error': 'Este correo ya está registrado'}
    )

        Usuario.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            password=password
        )

        return redirect('login')

    return render(request, 'usuarios/registro_admin.html')

def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(
                email=email,
                password=password
            )

            return redirect('admin_panel')

        except Usuario.DoesNotExist:
            return render(
                request,
                'usuarios/login_admin.html',
                {'error': 'Correo o contraseña incorrectos'}
            )

    return render(request, 'usuarios/login_admin.html')