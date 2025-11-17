from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from user.models import user_registration
# Create your views here.

def aadminhome(request):
    return render(request,"p_admin/aadminhome.html")
def DR(request):
     if request.method=="POST":
        FirstName=request.POST.get("firstname")
        LastName=request.POST.get("lastname")
        Gender=request.POST.get("gender")
        Email=request.POST.get("email") 
        ContactNumber=request.POST.get("contactno")
        Password=request.POST.get("password")
        Address=request.POST.get("message")
        Locality=request.POST.get("locality")
        Designation=request.POST.get("designation")
        Qualification=request.POST.get("qualification")
        Experience=request.POST.get("exp")
        Current_working_Place=request.POST.get("current_w_p")
        userdata=doctor_registration(FirstName=FirstName,LastName=LastName,Gender=Gender,Email=Email,ContactNumber=ContactNumber,Password=Password,Address=Address,Locality=Locality,Designation=Designation,Qualification=Qualification,Experience=Experience,Current_working_Place=Current_working_Place)
        userdata.save()
        return redirect("doctor_table")
        
     return render(request,"p_admin/DR.html")
def Usertable(request):
    Pro=user_registration.objects.all()
    return render(request,"p_admin/Usertable.html",{'P':Pro})
def doctor_table(request):
    DOC=doctor_registration.objects.all()
    return render(request,"p_admin/doctor_table.html",{'D':DOC})
def Admin_login(request):
    if request.method=="POST":
            try:
               
               email=request.POST.get("email")
               password=request.POST.get("password")
               log=table.objects.get(email=email,password=password)
               request.session['firstname']=log.email
               request.session['id']=log.id
               return redirect("aadminhome")
            except table.DoesNotExist:
               messages.info(request,'Invalid Login')
    return render(request,"p_admin/Admin_login.html")