from django.contrib import admin
from django.urls import path , include
from app.views import *

urlpatterns = [
    path('',home , name="home"),
    path('academics/',academics),
    path('facilities/',facilities),
    path('faculty/',faculty),
    path('gallery/',gallery),
    path('hostel/',hostel),
    path('labs/',labs),
    path('sports/',sports),
    path('about/',about),
    path('admission/',admission),
    path('contact/',contact),
    path('signup/',signup , name="signup"),
    path('login/',login , name="login"),
    path('logout/', logout , name="logout"),
]
