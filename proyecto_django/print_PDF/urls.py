from django.urls import path

from . import views

urlpatterns = [
    path("", views.print_PDF, name="front_page")
]