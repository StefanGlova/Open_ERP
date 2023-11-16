from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    emergency_contact = models.CharField(max_length=250)
    employment_start_date = models.DateField()
    employment_end_date = models.DateField(null=True)

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"

class EmploymentHistory(models.Model):
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    position = models.CharField(max_length=250)
    position_start_date = models.DateField()
    position_end_date = models.DateField(null=True)


class Positions(models.Model):
    pass