from django.shortcuts import render

# Create your views here.
def usuarioregister(request):
    return render(request, 'usuarioregister.html')