
from django.urls import path , include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("UserList/",views.UserList.as_view()),
    
    path("UserDetail/<int:pk>",views.UserDetail.as_view())
]