from django.urls import path
from . import views

urlpatterns = [
    path('registro_admin/', views.registro, name='registro_admin'),
    path('login_admin/', views.login_view, name='login_admin'),
]