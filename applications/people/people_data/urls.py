from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_data_home, name='people_data_home'),
    path('<int:id>', views.view_employee, name='view_employee'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete')
]
