from django.urls import path
from . import views

urlpatterns = [
    path('realizarprueba/', views.usuario_realizar_prueba, name="usuario_realizar_prueba")
]
