from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'), 
]
#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    . . . ,
    path('', views.index, name='index')
]
