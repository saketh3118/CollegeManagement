from django.urls import path
from user import views
urlpatterns = [
    path('',views.home),
    path('index',views.index),
    path('home',views.home),
    path('academics',views.academics),
    path('attendance',views.attendance),
    path('contactus',views.contactus)
]
