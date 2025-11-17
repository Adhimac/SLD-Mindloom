from django.urls import path
from .import views
urlpatterns = [
     path('doctorlogin',views.doctorlogin,name="doctorlogin"),
      path('doctorhome',views.doctorhome,name="doctorhome"),
      path('Pat_Appoin',views.Pat_Appoin,name="Pat_Appoin"),
      path('Pat_Result',views.Pat_Result,name="Pat_Result"),
      path('Pat_Test',views.Pat_Test,name="Pat_Test"),
      path('add_slot',views.add_slot,name="add_slot"),
   path('view_slot',views.view_slot,name="view_slot"),
]