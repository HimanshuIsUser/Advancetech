from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.icoderhome,name='icoderhome'),
    path('<str:slug>',views.icoderpost,name='icoderpost'),
]
