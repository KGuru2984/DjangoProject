from django.contrib import admin
from .models import Employees

# Register your models here.

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empName','empAddress')