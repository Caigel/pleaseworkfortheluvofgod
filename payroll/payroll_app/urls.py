from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_form, name='payroll_form'),
    path('calculate/', views.calculate_payroll, name='calculate_payroll'),
]
