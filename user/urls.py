from django.urls import path
from user import views
urlpatterns = [
    path('',views.home),
    path('index',views.index),
    path('home',views.home),
    path('academics',views.academics),
    path('attendance',views.attendance),
    path('contactus',views.contactus),
    path('assignments',views.assignments),
    path('mid1',views.mid1),
    path('mid2',views.mid2),
    path('marks',views.marks),
    path('logout',views.logout),
    path('logoutf',views.logoutf),
    path('faculty',views.faculty)
]
