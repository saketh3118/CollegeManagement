from django.db import models
from django.utils import timezone
class LoginDetails(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    usertype=models.CharField(max_length=30,default="usertype")
    dept=models.CharField(max_length=30,default="department")
    def __str__(self):
        return self.username
class Semester(models.Model):
    username=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    LANM=models.IntegerField()
    c1=models.CharField(max_length=10,default=4)
    EC=models.IntegerField()
    c2=models.CharField(max_length=10,default=4)
    BEEE=models.IntegerField()
    c3=models.CharField(max_length=10,default=3)
    PPS=models.IntegerField()
    c4=models.CharField(max_length=10,default=3)
    PPS_LAB=models.IntegerField(default=0)
    c5=models.CharField(max_length=10,default=3)
    EC_LAB=models.IntegerField()
    c6=models.CharField(max_length=10,default=1)
    BEEE_LAB=models.IntegerField()
    c7=models.CharField(max_length=10,default=1.5)
    IT_WORKSHOP=models.IntegerField()
    c8=models.CharField(max_length=10,default=1.5)
    ENG=models.IntegerField(default=0)
    c9=models.CharField(max_length=10,default=3)
    PandS=models.IntegerField(default=0)
    c10=models.CharField(max_length=10,default=3)
    SCP=models.IntegerField(default=0)
    c11=models.CharField(max_length=10,default=4)
    PYTHON=models.IntegerField(default=0)
    c12=models.CharField(max_length=10,default=4)
    EG=models.IntegerField(default=0)
    c13=models.CharField(max_length=10,default=3)
    ENG_LAB=models.IntegerField(default=0)
    c14=models.CharField(max_length=10,default=1)
    SCP_LAB=models.IntegerField(default=0)
    c15=models.CharField(max_length=10,default=1)
    PYTHON_LAB=models.IntegerField(default=0)
    c16=models.CharField(max_length=10,default=2)
    DM=models.IntegerField(default=0)
    c17=models.CharField(max_length=10,default=3)
    COA=models.IntegerField(default=0)
    c18=models.CharField(max_length=10,default=3)
    DS=models.IntegerField(default=0)
    c19=models.CharField(max_length=10,default=3)
    JAVA=models.IntegerField(default=0)
    c20=models.CharField(max_length=10,default=3)
    OS=models.IntegerField(default=0)
    c21=models.CharField(max_length=10,default=3)
    DS_LAB=models.IntegerField(default=0)
    c22=models.CharField(max_length=10,default=1.5)
    JAVA_LAB=models.IntegerField(default=0)
    c23=models.CharField(max_length=10,default=1.5)
    OS_LAB=models.IntegerField(default=0)
    c24=models.CharField(max_length=10,default=2)
    GS=models.IntegerField(default=0)
    c25=models.CharField(max_length=10,default=0)
    ASOT=models.IntegerField(default=0)
    c26=models.CharField(max_length=10,default=3)
    DBMS=models.IntegerField(default=0)
    c27=models.CharField(max_length=10,default=3)
    WT=models.IntegerField(default=0)
    c28=models.CharField(max_length=10,default=3)
    DAA=models.IntegerField(default=0)
    c29=models.CharField(max_length=10,default=3)
    CC=models.IntegerField(default=0)
    c30=models.CharField(max_length=10,default=3)
    DBMS_LAB=models.IntegerField(default=0)
    c31=models.CharField(max_length=10,default=2)
    WT_LAB=models.IntegerField(default=0)
    c32=models.CharField(max_length=10,default=1.5)
    DAA_LAB=models.IntegerField(default=0)
    c33=models.CharField(max_length=10,default=1.5)
    ES=models.IntegerField(default=0)
    c34=models.CharField(max_length=10,default=0)
    def __str__(self):
        return str(self.username)
class Attendance(models.Model):
    username=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    DM=models.IntegerField(default=0) 
    CNS=models.IntegerField(default=0) 
    EEA=models.IntegerField(default=0) 
    GB=models.IntegerField(default=0) 
    CD=models.IntegerField(default=0) 
    QA=models.IntegerField(default=0) 
    DM_LAB=models.IntegerField(default=0) 
    CD_LAB=models.IntegerField(default=0)
    ENG_LAB=models.IntegerField(default=0)
    def __str__(self):
        return str(self.username)
class TotalAttendance(models.Model):
    Dept=models.CharField(max_length=20,default="",primary_key=True)
    DM_TOTAL=models.IntegerField(default=0) 
    CNS_TOTAL=models.IntegerField(default=0) 
    EEA_TOTAL=models.IntegerField(default=0) 
    GB_TOTAL=models.IntegerField(default=0) 
    CD_TOTAL=models.IntegerField(default=0) 
    QA_TOTAL=models.IntegerField(default=0) 
    DM_LAB_TOTAL=models.IntegerField(default=0) 
    CD_LAB_TOTAL=models.IntegerField(default=0)
    ENG_LAB_TOTAL=models.IntegerField(default=0)
    def __str__(self):
        return self.Dept
class Queries(models.Model):
    name=models.CharField(primary_key=True,max_length=100,default=0)
    username=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    text=models.TextField()
    def __str__(self):
        return str(self.username)
class TimeTable(models.Model):
    date=models.DateTimeField(default=timezone.now)
    Year=models.IntegerField()
    Dept=models.CharField(max_length=20)
    Day=models.CharField(max_length=20,default="sunday",primary_key=True)
    C1=models.CharField(max_length=20)
    C2=models.CharField(max_length=20)
    C3=models.CharField(max_length=20)
    C4=models.CharField(max_length=20)
    C5=models.CharField(max_length=20)
    C6=models.CharField(max_length=20)
    C7=models.CharField(max_length=20,default="")
    def __str__(self):
        return str(self.Year)+"   "+self.Dept+"   "+self.Day
class Assignments(models.Model):
    sub=models.CharField(max_length=30,default="",primary_key=True)
    mid=models.CharField(max_length=200,default="mid")
    q1=models.CharField(max_length=200,default="",blank=True)
    q2=models.CharField(max_length=200,default="",blank=True)
    q3=models.CharField(max_length=200,default="",blank=True)
    q4=models.CharField(max_length=200,default="",blank=True)
    q5=models.CharField(max_length=200,default="",blank=True)
    q6=models.CharField(max_length=200,default="",blank=True)
    q7=models.CharField(max_length=200,default="",blank=True)
    q8=models.CharField(max_length=200,default="",blank=True)
    q9=models.CharField(max_length=200,default="",blank=True)
    q10=models.CharField(max_length=200,default="",blank=True)
    def __str__(self):
        return self.sub
class Mid1(models.Model):
    username=models.CharField(max_length=30,default="",primary_key=True)
    name=models.CharField(max_length=50,default="")
    Java_Programming_Cse=models.CharField(max_length=10,blank=True)
    Data_Structures_Cse=models.CharField(max_length=10,blank=True)
    Web_Technologies_Cse=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.username
class Mid2(models.Model):
    username=models.CharField(max_length=30,default="")
    name=models.CharField(max_length=50,default="",primary_key=True)
    Java_Programming_Cse=models.CharField(max_length=10,blank=True)
    Data_Structures_Cse=models.CharField(max_length=10,blank=True)
    Web_Technologies_Cse=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.username
class Materials(models.Model):
    material=models.FileField()
class Message(models.Model):
    message_id=models.IntegerField()
    sender=models.CharField(max_length=120)
    receiver=models.CharField(max_length=120)
    message=models.CharField(max_length=1000,blank=False)
    timestamp=models.DateTimeField(default=timezone.now)
    def __str__(self):
        id=str(self.message_id)
        return "message id "+id+" "+self.sender+" to "+self.receiver