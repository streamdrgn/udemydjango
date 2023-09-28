from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    my_title = "Hello there..."
    return render(request, "base.html")

def about_page(request):
    return render(request, "about.html", {"title": "About"})

def example_page(request):
    context = {"title": "Example"}
    something_here = "hello_world.html"
    return HttpResponse(something_here) render(request, "hello_world.html", {"title": "Contact us"})
