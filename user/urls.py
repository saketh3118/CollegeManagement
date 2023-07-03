from django.urls import path
from user import views
urlpatterns = [
    path('',views.home),
    path('index',views.index),
    path('home',views.home),
    path('attendance',views.attendance),
    path('contactus',views.contactus),
    path('assignments',views.assignments),
    path('mid1',views.mid1),
    path('mid2',views.mid2),
    path('marks',views.marks),
    path('logout',views.logout),
    path('logoutf',views.logoutf),
    path('faculty',views.faculty),
    path('admins',views.admin),
    path('addusers',views.addusers),
    path('adduserdetails',views.adduserdetails),
    path('edituser.html/<str:pk>',views.edituser,name="edituser"),
    path('deleteuser.html/<str:pk>',views.deleteuser,name="deleteuser"),
    path('savechanges',views.savechanges),
    path('listofsems',views.listofsems),
    path('edituserresults/<str:pk>/<str:sem>',views.edituserresults,name="edituserresults"),
    path('sem1',views.sem1),
    path('sem2',views.sem2),
    path('sem3',views.sem3),
    path('sem4',views.sem4),
    path('edituserresults/<str:pk>/<str:sem>',views.edituserresults,name="edituserresults"),
    path('timetable',views.timetable),
    path('editattendance',views.editattendance),
    path('edituserattendance/<str:pk>',views.edituserattendance,name="edituserattendance"),
    path('midmarks1',views.midmarks1),
    path('midmarks2',views.midmarks2),
    path('semresults',views.semresults),
    path('mid',views.mid),
    path('assignmentquestions',views.assign),
    path('displaytimetable',views.displaytimetable)
]



# <a href="{% url 'edituser' pk=user.username %}">