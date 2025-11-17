from django.db import models

# Create your models here.
class table(models.Model):
    Name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=75)


class doctor_registration(models.Model):
    FirstName=models.CharField(max_length=25)
    LastName=models.CharField(max_length=25)
    Gender=models.CharField(max_length=10)
    Email=models.EmailField(max_length=50)
    ContactNumber=models.CharField(max_length=10)
    Password=models.CharField(max_length=25,null=True)
    Address=models.CharField(max_length=50)
    Locality=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=50)
    Experience=models.IntegerField(max_length=50)
    Current_working_Place=models.CharField(max_length=50)
    status=models.BooleanField(max_length=25,default="False")
