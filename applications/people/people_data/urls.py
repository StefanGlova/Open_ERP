from django.urls import path
from . import views

urlpatterns = [
    path('people_data/', views.people_data_home, name='people_data_home'),
    path('people_data/<int:id>', views.view_employee, name='view_employee'),
    path('people_data/add/', views.add, name='add'),
    path('people_data/edit/<int:id>', views.edit, name='edit'),
    path('people_data/delete/<int:id>', views.delete, name='delete')
]
