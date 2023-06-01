from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "proyecto_djangoApp/home.html")

def servicios(request):
    return render(request, "proyecto_djangoApp/servicios.html")

def contacto(request):
    return render(request, "proyecto_djangoApp/contacto.html")