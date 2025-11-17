
from django.urls import path,include
from .import views
urlpatterns = [
    path('aadminhome',views.aadminhome,name="aadminhome"),
    path('DR',views.DR,name="DR"),
    path('Usertable',views.Usertable,name="Usertable"),
    path('Admin_login',views.Admin_login,name="Admin_login"),
    path('doctor_table',views.doctor_table,name="doctor_table"),
]
