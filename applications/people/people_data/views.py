from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Employee
from .forms import EmployeeForm

def people_data_home(request):
    return render(request, 'people_data/home_people_data.html', {
        'employees': Employee.objects.all()
    })

def view_employee(request, id):
    employee = Employee.objects.get(pk=id)
    return HttpResponseRedirect(reverse('people_data_home'))

def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_address = form.cleaned_data['address']
            new_phone = form.cleaned_data['phone']
            new_email = form.cleaned_data['email']
            new_emergency_contact = form.cleaned_data['emergency_contact']
            new_employment_start_date = form.cleaned_data['employment_start_date']

            new_employee = Employee(
                first_name = new_first_name,
                last_name = new_last_name,
                address = new_address,
                phone = new_phone,
                email = new_email,
                emergency_contact = new_emergency_contact,
                employment_start_date = new_employment_start_date,
            )

            new_employee.save()
            return render(request, 'people_data/add_people_data.html', {
                'form': EmployeeForm(),
                'success': True
            })
    else:
        form = EmployeeForm()
    return render(request, 'people_data/add_people_data.html', {
        'form': EmployeeForm()
    })

def edit(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return render(request, 'people_data/edit_people_data.html', {
                'form': form,
                'success': True,
                'employee': employee
            })
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'people_data/edit_people_data.html', {
        'form': form,
        'employee': employee
    })

def delete(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=id)
        employee.delete()
    return HttpResponseRedirect(reverse('people_data_home'))
    
    