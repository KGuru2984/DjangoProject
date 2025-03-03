from django.shortcuts import render
from django.http import HttpResponse
from EmployeeDetails.models import Employees 

# Create your views here.

def AddRecord(request):
    emp1=Employees.objects.create(
        empName='ITVedant',
        empAddress='Dadar'
    )
    return HttpResponse('Welcome to Employee Addition Page!')