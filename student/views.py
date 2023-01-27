from django.shortcuts import render
from .models import stdnt

# Create your views here.
def index(request):
    return render(request, "student/index.html", {
        'students': stdnt.objects.all()
    })
    