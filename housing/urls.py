from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('',views.getRoutes,name="routes"),
    path('housing/',views.getHousing,name="housing"),
    path('housing/<str:pk>',views.getHouse,name="house"),
]