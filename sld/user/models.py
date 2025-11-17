from django.db import models

# Create your models here.
class user_registration(models.Model):
    ParentName=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=75)
    phoneNumber=models.CharField(max_length=15)
    ChildName=models.CharField(max_length=25)
    age=models.IntegerField(max_length=2)
    gender=models.CharField(max_length=10)
    standard=models.IntegerField(max_length=2)
    syllabus=models.CharField(max_length=10)

    # def __str__(self):
    #     return self.user_registration