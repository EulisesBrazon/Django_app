from django.shortcuts import render
from django.http import HttpResponse
from .funtions import render_to_pdf


def print_PDF(request):
    #return render(request, "print_PDF/front_page.html") 
    pdf = render_to_pdf("print_PDF/front_page.html")
    return HttpResponse(pdf, content_type = "application/pdf")

