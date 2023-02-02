from django import forms
from .models import stdnt


class studentForm(forms.ModelForm):
    class Meta:
        model = stdnt
        fields = ['student_name', 'first_name', 'last_name', 'email', 'course', 'gpa' ]
        labels = {'student_name': 'Student Number', 
                'first_name': 'First Name', 
                'last_name': 'Last Name',
                 'email': 'Email', 
                 'course': 'Field of study',
                  'gpa': 'GPA'}

        widget = {
            'student_name': forms.NumberInput(attrs={'class':'mb-6'}), 
            'first_name': forms.TextInput(attrs={'class':'mb-6'}), 
            'last_name':forms.TextInput(attrs={'class':'mb-6'}), 
            'email':forms.EmailInput(attrs={'class':'mb-6'}), 
            'course': forms.TextInput(attrs={'class':'mb-6'}), 
            'gpa': forms.NumberInput(attrs={'class':'mb-6'})
        }