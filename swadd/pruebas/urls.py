from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuarioregister, name="usuario_register")
]
