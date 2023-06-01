from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    if request.user.is_authenticated:
        # Do something for authenticated users.
        user_name = request.user.username
        return render(request, "proyecto_djangoApp/home.html", {'nombre': user_name})
    
    else:
        # Do something for anonymous users.
        user_name = "Anonymous"
        return render(request, "proyecto_djangoApp/home.html", {'nombre': user_name})

def perfil(request):

    if request.user.is_authenticated:
        # Do something for authenticated users.
        user_id = request.user.id
        user_name = request.user.username
        user_email = request.user.email

        return render(request, "proyecto_djangoApp/perfil.html", {'id': user_id, 'nombre': user_name, 'email': user_email})
    
    else:
        # Do something for anonymous users.
        return render(request, "proyecto_djangoApp/perfil.html")

def informacion(request):
    return render(request, "proyecto_djangoApp/informacion.html")