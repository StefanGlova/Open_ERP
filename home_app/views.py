from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home_app/home.html')

def people(request):
    return render(request, 'home_app/people.html')

def operation(request):
    return render(request, 'home_app/operation.html')

def customers(request):
    return render(request, 'home_app/customers.html')

def finance(request):
    return render(request, 'home_app/finance.html')

def projects(request):
    return render(request, 'home_app/projects.html')

def KPIs(request):
    return render(request, 'home_app/KPIs.html')

def about(request):
    return render(request, 'home_app/about.html')