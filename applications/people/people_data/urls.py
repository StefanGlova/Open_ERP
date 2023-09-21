from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_data_home, name='people_data_home'),
]
