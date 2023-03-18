from rest_framework import serializers
from EmployeeApp.models import Departments,Employes

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employes
        fields=('EmployeetId','EmployeesName','Department','DateOfJoining','PhotoFileName')