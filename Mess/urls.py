from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Mess import views

urlpatterns = [
    path('test/',views.MessTest.as_view()),
    path('mess/', views.MessList.as_view()),
    path('mess/<int:pk>/', views.MessDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)