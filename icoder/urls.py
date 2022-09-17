from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('postcomment',views.postcomment,name='postcomment'),

    path('',views.icoderhome,name='icoderhome'),
    path('<str:slug>',views.icoderpost,name='icoderpost')
]
