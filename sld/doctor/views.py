from django.shortcuts import render

# Create your views here.
def doctorlogin(request):
    return render(request,"Doctor/doctorlogin.html")
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
def view_slot(request):
    return render(request,"Doctor/view_slot.html")