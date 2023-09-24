from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'address',
            'phone',
            'email',
            'emergency_contact',
            'employment_start_date'
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address': 'Address',
            'phone': 'Phone Number',
            'email': 'Email',
            'emergency_contact': 'Emergency Contact (Name and phone number)',
            'employment_start_date': 'Employment Start Date'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'employment_start_date': forms.DateInput(attrs={'class': 'form-control'})
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     # Set 'required' attribute to False for employment_end_date
    #     self.fields['employment_end_date'].required = False