from django.contrib import admin
from django.urls import path,include
from .views import *
# from Admin.urls import *

urlpatterns = [
    path('',Index),
    path('cart/',Cart),
    path('contact/',Contact1),
    path('send_msg/',Send_Msg),
    path('add_cart/',Add_to_Cart),
    path('blog/',Blog),
    path('login/',LoginView.as_view() , name='login_url'),
    path('register/',Register,name='register_url'),
    path('logout/',Logout),
    path('karta/',Karta,name='karta')
]