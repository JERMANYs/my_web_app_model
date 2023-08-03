from django.shortcuts import render, HttpResponse  
from . import models
# Create your views here.
def home(request):
    context = {}

    students = models.student.objects.all().order_by("-id")

    context = {
        'students' : students,
    }

    return render(request, 'index.html', context)
   

def about(request):
    return render(request, 'about.html')
    

def contact(request):
    return render(request, 'contact.html')

def studentdetails(request, id) :
    context = {}
    student = models.student.objects.get(id=id)
    context['student'] = student
    return render (request, 'details.html', context)