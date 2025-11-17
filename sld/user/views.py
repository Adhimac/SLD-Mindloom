from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def userreg(request):
    if request.method=="POST":
        ParentName=request.POST.get("ParentName")
        email=request.POST.get("Email")
        password=request.POST.get("password")
        ConfirmPassowrd=request.POST.get("ConfirmPassowrd") 
        phoneNumber=request.POST.get("phoneNumber")
        ChildName=request.POST.get("ChildName")
        age=request.POST.get("age")
        gender=request.POST.get("gender")
        standard=request.POST.get("standard")
        syllabus=request.POST.get("syllabus")
        if password==ConfirmPassowrd:
            if  user_registration.objects.filter(email=email).exists():
                messages.info(request,'This Email is already exists')
            elif  user_registration.objects.filter(phoneNumber=phoneNumber).exists():
                    messages.info(request,'This Phone Number is already exists')
            else:
                userdata=user_registration(ParentName=ParentName,email=email,password=password,phoneNumber=phoneNumber,ChildName=ChildName,age=age,gender=gender,standard=standard,syllabus=syllabus)
                userdata.save()
                return redirect("userlogin")
        else:
            messages.info(request,"Password are not matching")
    return render(request,"User/userreg.html")
def userlogin(request):
    if request.method=="POST":
           try:
               ParentName=request.POST.get("Username")
               email=request.POST.get("email")
               password=request.POST.get("password")
               log=user_registration.objects.get(email=email,password=password,ParentName=ParentName)
               request.session['firstname']=log.ParentName
               request.session['id']=log.id
               return redirect("userhome")
           except user_registration.DoesNotExist:
               messages.info(request,'Invalid Login')
    return render(request,"User/userlogin.html")
def userhome(request):

    return render(request,"User/userhome.html")
def doctors(request):
    return render(request,"User/doctors.html")
def doctor1(request):
    return render(request,"User/doctor1.html")
def booking(request):
    return render(request,"User/booking.html")
def appointment(request):
    return render(request,"User/appointment.html")
def About(request):
    return render(request,"User/About.html")