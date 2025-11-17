from django.urls import path
from .import views
urlpatterns=[
    path('userreg',views.userreg,name="userreg"),
     path('userlogin',views.userlogin,name="userlogin"),
     path('userhome',views.userhome,name="userhome"),
      path('doctors',views.doctors,name="doctors"),
      path('doctor1',views.doctor1,name="doctor1"),
      path('booking',views.booking,name="booking"),
      path('appointment',views.appointment,name="appointment"),
      path('About',views.About,name="About"),
    
    
]