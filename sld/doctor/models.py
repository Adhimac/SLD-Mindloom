from django.db import models
from  P_admin.models import *
# Create your models here.
class DoctorSlot(models.Model):
    doctor = models.ForeignKey(doctor_registration, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)

    start_time = models.TimeField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.doctor} - {self.day}"