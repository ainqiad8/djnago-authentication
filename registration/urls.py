from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registrationform, name="registrationform"),
    path("", views.homepage, name="homepage"),

    path('loginPage/', views.loginPage, name="loginPage"),

    path('logout', views.logoutPage, name = "logoutPage"),
]
