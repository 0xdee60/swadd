from django.shortcuts import render

# Create your views here.
def usuario_realizar_prueba(request):
    return render(request, 'usuario_realizar_prueba.html')