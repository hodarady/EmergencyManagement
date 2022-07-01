

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.signin , name = 'signin' ) ,
    path('logout' , views._logout , name = "logout") ,
    path('services' , views.services , name = 'services') ,
    path('new_resident' , views.form2 , name = 'new_resident') ,
    path('new_patient'  , views.form1 , name = 'new_patient') ,
    path('display_patients' , views.display_patients , name = 'display_patients') ,
    path('rooms' , views.rooms , name = 'rooms') ,
    # path('addExitTime' , views.addExitTime , name = 'addExitTime') ,
    path('showProfileInfo' , views.showProfileInfo , name = 'showProfileInfo') ,
    path('search' , views.search , name = 'search') ,
    path('editExitTime/<str:pk>' , views.editExitTime , name = 'editExitTime') ,
    path('invoice' , views.invoice , name = "invoice")
]
