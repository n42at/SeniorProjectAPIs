from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView, UserView,LogoutView, PatientView,AddPatientView
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('patient', PatientView.as_view()),
    path('AddPatient', AddPatientView.as_view())

]





#, RegisterView, LoginVie

#LogoutView,UserView