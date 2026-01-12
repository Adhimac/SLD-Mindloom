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
#path('take_test/<str:disorder_name>/', views.take_test, name="take_test"),

     # Screening flow (all 3 tests one-by-one)
    path("start_screening/", views.start_screening, name="start_screening"),
    path("take_test/<str:disorder_name>/", views.take_test, name="take_test"),
    path("submit_test/<str:disorder_name>/", views.submit_test, name="submit_test"),
    path("screening_summary/", views.screening_summary, name="screening_summary"),
    path("reset_attempts/", views.reset_attempts, name="reset_attempts"),

]