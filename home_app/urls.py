from django.urls import path
from home_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('people/', views.people, name='people'),
    path('operation/', views.operation, name='operation'),
    path('customers/', views.customers, name='customers'),
    path('finance/', views.finance, name='finance'),
    path('projects/', views.projects, name='projects'),
    path('KPIs/', views.KPIs, name='KPIs')
]
