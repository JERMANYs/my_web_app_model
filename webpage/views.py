from django.shortcuts import render, HttpResponse  

# Create your views here.
def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, this is my home page django app")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About me")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("Contact me")