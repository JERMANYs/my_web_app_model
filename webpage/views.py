from django.shortcuts import render, HttpResponse  

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is my first home page django app")

def about(request):
    return HttpResponse("About us")

def contact(request):
    return HttpResponse("Contact us")