from django import forms
from .models import Student
from datetime import date

class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    class Meta:
        model = Student
        fields = ['student_name',
                   'father_name',
                     'mother_name', 
                     'student_class', 
                     'school_name', 
                     'student_aadhar', 
                     'father_aadhar',
                       'mother_aadhar',
                       'mobile_number',
                       'dob',
                       'age',
                       'address',
                       'image'
                       ]
    