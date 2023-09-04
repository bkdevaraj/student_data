from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    student_name = forms.CharField(max_length=150)
    father_name = forms.CharField(max_length=150)
    mother_name = forms.CharField(max_length=150)
    student_class = forms.CharField(max_length=150)
    school_name = forms.CharField(max_length=150)
    student_aadhar = forms.CharField(max_length=150)
    father_aadhar = forms.CharField(max_length=150)
    mother_aadhar = forms.CharField(max_length=150)
    mobile_number = forms.CharField(max_length=150)
    address = forms.CharField(max_length=500, initial='Unknown')
    image = forms.ImageField(required=False)
    remarks = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Student
        fields = ['student_name', 'father_name', 'mother_name', 'student_class', 'school_name', 'student_aadhar', 'father_aadhar', 'mother_aadhar', 'mobile_number', 'dob', 'age', 'address', 'image', 'remarks']
