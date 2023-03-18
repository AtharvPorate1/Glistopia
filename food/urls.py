from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    
    path('',views.getFood,name="food"),
    #path('food/<str:pk>',views.getMess,name="Mess"),
]