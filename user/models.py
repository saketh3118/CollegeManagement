from django.db import models
from django.utils import timezone
# Create your models here.
class LoginDetails(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=50,default="")
    usertype=models.CharField(max_length=30,default="usertype")
    dept=models.CharField(max_length=30,default="department")
    def __str__(self):
        return self.username
class Semester(models.Model):
    username=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    LANM=models.IntegerField()
    EC=models.IntegerField()
    BEEE=models.IntegerField()
    PPS=models.IntegerField()
    PPS_LAB=models.IntegerField(default=0)
    EC_LAB=models.IntegerField()
    BEEE_LAB=models.IntegerField()
    IT_WORKSHOP=models.IntegerField()
    TotalCredits1=models.IntegerField(default=0)
    ENG=models.IntegerField(default=0)
    PandS=models.IntegerField(default=0)
    SCP=models.IntegerField(default=0)
    PYTHON=models.IntegerField(default=0)
    EG=models.IntegerField(default=0)
    ENG_LAB=models.IntegerField(default=0)
    SCP_LAB=models.IntegerField(default=0)
    PYTHON_LAB=models.IntegerField(default=0)
    TotalCredits2=models.IntegerField(default=0)
    DM=models.IntegerField(default=0)
    COA=models.IntegerField(default=0)
    DS=models.IntegerField(default=0)
    JAVA=models.IntegerField(default=0)
    OS=models.IntegerField(default=0)
    DS_LAB=models.IntegerField(default=0)
    JAVA_LAB=models.IntegerField(default=0)
    OS_LAB=models.IntegerField(default=0)
    GS=models.IntegerField(default=0)
    TotalCredits3=models.IntegerField(default=0)
    ASOT=models.IntegerField(default=0)
    DBMS=models.IntegerField(default=0)
    WT=models.IntegerField(default=0)
    DAA=models.IntegerField(default=0)
    CC=models.IntegerField(default=0)
    DBMS_LAB=models.IntegerField(default=0)
    WT_LAB=models.IntegerField(default=0)
    DAA_LAB=models.IntegerField(default=0)
    ES=models.IntegerField(default=0)
    TotalCredits4=models.IntegerField(default=0)
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
        return str(self.username)
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
    Day=models.CharField(max_length=20,default="sunday")
    C1=models.CharField(max_length=20)
    C2=models.CharField(max_length=20)
    C3=models.CharField(max_length=20)
    C4=models.CharField(max_length=20)
    C5=models.CharField(max_length=20)
    C6=models.CharField(max_length=20)
    C7=models.CharField(max_length=20,default="sports")
    def __str__(self):
        return str(self.Year)+"   "+self.Dept+"   "+self.Day
class Assignments(models.Model):
    sub=models.CharField(max_length=30,default="",primary_key=True)
    mid=models.CharField(max_length=200,default="mid")
    q1=models.CharField(max_length=200,default="text",blank=True)
    q2=models.CharField(max_length=200,default="text",blank=True)
    q3=models.CharField(max_length=200,default="text",blank=True)
    q4=models.CharField(max_length=200,default="text",blank=True)
    q5=models.CharField(max_length=200,default="text",blank=True)
    q6=models.CharField(max_length=200,default="text",blank=True)
    q7=models.CharField(max_length=200,default="text",blank=True)
    q8=models.CharField(max_length=200,default="text",blank=True)
    q9=models.CharField(max_length=200,default="text",blank=True)
    q10=models.CharField(max_length=200,default="text",blank=True)
    def __str__(self):
        return self.sub
class Mid1(models.Model):
    username=models.CharField(max_length=30,default="",primary_key=True)
    Java_Programming_Cse=models.CharField(max_length=10,blank=True)
    Data_Structures_Cse=models.CharField(max_length=10,blank=True)
    Web_Technologies_Cse=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.username
class Mid2(models.Model):
    username=models.CharField(max_length=30,default="",primary_key=True)
    Java_Programming_Cse=models.CharField(max_length=10,blank=True)
    Data_Structures_Cse=models.CharField(max_length=10,blank=True)
    Web_Technologies_Cse=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.username