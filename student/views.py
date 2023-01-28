from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import stdnt

# Create your views here.
def index(request):
    return render(request, "student/index.html", {
        'students': stdnt.objects.all()
    })

# View students 
def view_student(request, id):
    student = stdnt.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
    