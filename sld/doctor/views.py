from django.shortcuts import render,redirect
from P_admin.models import doctor_registration
from datetime import time
from .models import *
from django.contrib import messages
# Create your views here.
def doctorlogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        log = doctor_registration.objects.filter(
            Email=email,
            Password=password
        ).first()

        if log:
            request.session['Email'] = log.Email
            request.session['id'] = log.id
            return redirect("doctorhome")
        else:
            messages.error(request, "Invalid Email or Password")

    return render(request, "Doctor/doctorlogin.html")
def doctorhome(request):
    return render(request,"Doctor/doctorhome.html")
def Pat_Appoin(request):
    return render(request,"Doctor/Pat_Appoin.html")
def Pat_Result(request):
    return render(request,"Doctor/Pat_Result.html")
def Pat_Test(request):
    return render(request,"Doctor/Pat_Test.html")
def add_slot(request):
    return render(request,"Doctor/add_slot.html")



from datetime import time
from django.shortcuts import render, redirect
from .models import DoctorSlot, doctor_registration

def add_slot(request):
    if request.method == "POST":

        # get doctor ID from session
        doctor_id = request.session.get('id')

        # fetch doctor object
        doctor = doctor_registration.objects.get(id=doctor_id)

        days = request.POST.getlist("days[]")

        for day in days:
            sh = int(request.POST.get(f"{day.lower()}_start_hour"))
            sm = int(request.POST.get(f"{day.lower()}_start_minute"))
            sap = request.POST.get(f"{day.lower()}_start_ampm")

            eh = int(request.POST.get(f"{day.lower()}_end_hour"))
            em = int(request.POST.get(f"{day.lower()}_end_minute"))
            eap = request.POST.get(f"{day.lower()}_end_ampm")

            # AM/PM → 24 hour conversion
            if sap == "PM" and sh != 12:
                sh += 12
            if sap == "AM" and sh == 12:
                sh = 0

            if eap == "PM" and eh != 12:
                eh += 12
            if eap == "AM" and eh == 12:
                eh = 0

            start_time = time(sh, sm)
            end_time = time(eh, em)

            DoctorSlot.objects.create(
                doctor=doctor,   # ✅ OBJECT, not ID
                day=day,
                start_time=start_time,
                end_time=end_time
            )

        return redirect("doctorhome")

    return render(request, "Doctor/add_slot.html")

    
def view_slot(request):
    doctor_id = request.session.get('id')
    doctor = doctor_registration.objects.get(id=doctor_id)

    slots = DoctorSlot.objects.filter(doctor=doctor).order_by('day', 'start_time')

    return render(request, "Doctor/view_slot.html", {
        "slots": slots
    })
