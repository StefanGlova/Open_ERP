from django.shortcuts import render

# Create your views here.
def people_data_home(request):
    return render(request, 'people_data/home.html')