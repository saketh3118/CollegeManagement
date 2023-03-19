from django.contrib import admin
from user.models import LoginDetails,Semester,Attendance,Queries,TimeTable,Assignments
# Register your models here.
admin.site.register(LoginDetails)
admin.site.register(Semester)
admin.site.register(Attendance)
admin.site.register(Queries)
admin.site.register(TimeTable)
admin.site.register(Assignments)
