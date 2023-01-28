from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import stdnt
from .forms import studentForm

# Create your views here.
def index(request):
    return render(request, "student/index.html", {
        'students': stdnt.objects.all()
    })

# View students 
def view_student(request, id):
    student = stdnt.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

# Add student
def add(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_name']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_course = form.cleaned_data['course']
            new_gpa = form.cleaned_data['gpa']

            new_student = stdnt(student_name = new_student_number,
            first_name = new_first_name,
            last_name = new_last_name,
            email = new_email,
            course = new_course,
            gpa= new_gpa
            )
            new_student.save()
            return render(request, 'student/add.html', {
                'form': studentForm(),
                'success': True
            })
    else:
        form = studentForm()
    return render(request, 'student/add.html', {
            'form': studentForm()
        })

# Edit student
def edit(request, id):
    if request.method == "POST":
        student = stdnt.objects.get(pk=id)
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = stdnt.objects.get(pk=id)
        form = studentForm(instance=student)
    return render(request, 'student/edit.html', {
        'form': form
    })         
    
