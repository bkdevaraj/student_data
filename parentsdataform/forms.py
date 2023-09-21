from django import forms
from .models import Parent

class ParentForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=150)
    middle_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    occupation = forms.CharField(max_length=150)
    aadhar_number = forms.CharField(max_length=150)
    pan_number = forms.CharField(max_length=150)
    has_disability = forms.BooleanField(
        required=False,  # Not required, as it's a True/False choice.
        widget=forms.CheckboxInput(attrs={'class': 'tgl tgl-light'}),
        label='Has Disability',  # Label for the checkbox.
    )
    pension_eligible = forms.BooleanField(
        required=False,  # Not required, as it's a True/False choice.
        widget=forms.CheckboxInput(attrs={'class': 'tgl tgl-light'}),
        label='Pension Eligible',  # Label for the checkbox.
    )
    mobile_number = forms.CharField(max_length=150)
    pension_amount=forms.DecimalField(max_digits=10, decimal_places=2)
    dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    address = forms.CharField(max_length=500, initial='Unknown')
    image = forms.ImageField(required=False)
    remarks = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Parent
        fields = [
            'first_name','middle_name' ,'last_name','occupation', 'aadhar_number', 'pan_number', 'has_disability',
            'pension_eligible','dob', 'mobile_number', 'pension_amount', 'address', 'image', 'remarks'
        ]
