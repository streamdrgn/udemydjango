from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "global/base.html")

def about_page(request):
    return HttpResponse("<h1>This is about page!</h1>")
