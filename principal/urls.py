from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('canchas/', views.canchas, name='canchas'),
    path('reservas/', views.reservas, name='reservas'),
    path('formulario/', views.formulario, name='formulario'),
    path('pago/', views.pago, name='pago'),
    
    # Rutas del módulo de administración
    path('dashboard/', views.inicio_admi, name='inicio_admi'),
    path('panel-admin/', views.admin_panel, name='admin_panel'),
]