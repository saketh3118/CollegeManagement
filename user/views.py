from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from user.models import *
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if(user is not None):
            return render(request,'admin.html')
        try:
            lg=LoginDetails.objects.get(username=username)
        except :
            return render(request,'home.html')
        if(lg.username==username and lg.password==password):
            request.session['uname']=lg.username
            request.session['name']=lg.name
            if(lg.usertype=="Faculty"):
                fac=LoginDetails.objects.get(username=request.session.get('uname'))
                return render(request,'faculty.html',{'fac':fac})
            return render(request,'index.html',{'lg':lg,'uname':lg.username,'name':lg.name})
    return render(request,'home.html',{})
def index(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    return render(request,'index.html',{'uname':uname,'name':name}) 
def academics(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    s=Semester.objects.get(username=uname)
    sum1=0.0
    l=[4,4,3,3,1.5,1,1,1.5,3,3,4,4,3,1,1,2,3,3,3,3,3,1.5,1.5,2,0,3,3,3,3,3,2,1.5,1.5,0]
    j=0
    for i in [s.LANM,s.EC,s.BEEE,s.PPS,s.PPS_LAB,s.EC_LAB,s.BEEE_LAB,s.IT_WORKSHOP]:
        sum1=sum1+i*l[j]
        j=j+1
    sum1=sum1/s.TotalCredits1
    sum1=round(sum1,2)
    sum2=0.0
    for i in [s.ENG,s.PandS,s.SCP,s.PYTHON,s.EG,s.ENG_LAB,s.SCP_LAB,s.PYTHON_LAB]:
        sum2=sum2+i*l[j]
        j=j+1
    sum2=sum2/s.TotalCredits2
    sum2=round(sum2,2)
    sum3=0.0
    for i in [s.DM,s.COA,s.DS,s.JAVA,s.OS,s.DS_LAB,s.JAVA_LAB,s.OS_LAB,s.GS]:
        sum3=sum3+i*l[j]
        j=j+1
    sum3=sum3/s.TotalCredits3
    sum3=round(sum3,2)
    sum4=0.0
    for i in [s.ASOT,s.DBMS,s.WT,s.DAA,s.CC,s.DBMS_LAB,s.WT_LAB,s.DAA_LAB,s.ES]:
        sum4=sum4+i*l[j]
        j=j+1
    sum4=sum4/s.TotalCredits3
    sum4=round(sum4,2)
    avg=round((sum1+sum2+sum3+sum4)/4,2)
    temp=avg
    v1=temp*10
    tt=TimeTable.objects.all()
    assignments=Assignments.objects.all()
    m1=Mid1.objects.get(username=uname)
    m2=Mid2.objects.get(username=uname)
    return render(request,'academics.html',{'s':s,'uname':uname,'name':name,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'avg':avg,'tt':tt,'date':tt[0].date.date(),'v1':v1,'assignments':assignments,'m1':m1,'m2':m2})
def attendance(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    a=Attendance.objects.get(username=uname)
    sum1=0.0
    sum2=0.0
    for i in [a.DM,a.CNS,a.EEA,a.GB,a.CD,a.QA,a.DM_LAB,a.CD_LAB,a.ENG_LAB]:
        sum1=sum1+i
    for i in [a.DM_TOTAL,a.CNS_TOTAL,a.EEA_TOTAL,a.GB_TOTAL,a.CD_TOTAL,a.QA_TOTAL,a.DM_LAB_TOTAL,a.CD_LAB_TOTAL,a.ENG_LAB_TOTAL]:
        sum2=sum2+i
    percentage=round((sum1*100)/sum2,2)
    msg=""
    if(percentage>=65 and percentage<75):
        msg="You're Close to 75% Attendance,Come Regular to Improve"
    elif(percentage>=75):
        msg="Hurray!!You are Elgible for Attending Exams"
    elif(percentage<65):
        msg="You are in Dangerzone Come regular to avoid Detention"
    ans=round(percentage,2)
    return render(request,'attendance.html',{'uname':uname,'name':name,'a':a,'msg':msg,'percentage':ans,'v1':ans})
def contactus(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    val=0
    if request.method=='POST':
        uname=request.session.get('uname')
        name=request.session.get('name')
        text=request.POST.get('text')
        obj=Queries.objects.get(username=uname)
        obj.name=name
        obj.text=text
        obj.save()
        val=1
        return render(request,'contactus.html',{'uname':uname,'name':name,'val':val})
    val=0
    return render(request,'contactus.html',{'uname':uname,'name':name,'val':val})
def assignments(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    return render(request,'assignments.html',{'fac':fac})
def mid1(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    if request.method=='POST':
        sub=fac.dept
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')
        q5=request.POST.get('q5')
        try:
            text=Assignments.objects.create(sub=sub,mid="Mid1",q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
            text.save()
        except:
            text=Assignments.objects.get(sub=sub)
            text.mid="Mid1"
            text.q1=request.POST.get('q1')
            text.q2=request.POST.get('q2')
            text.q3=request.POST.get('q3')
            text.q4=request.POST.get('q4')
            text.q5=request.POST.get('q5')
            text.save()
        messages.success(request,'Success!Assignment Questions has been Posted')
        return render(request,'mid1.html',{'fac':fac,'ans':text,'flag':1})
    ans=Assignments.objects.get(sub=fac.dept)
    ans.mid="Mid1"
    return render(request,'mid1.html',{'fac':fac,'ans':ans,'flag':-1})
def mid2(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    if request.method=='POST':
        sub=fac.dept
        q6=request.POST.get('q6')
        q7=request.POST.get('q7')
        q8=request.POST.get('q8')
        q9=request.POST.get('q9')
        q10=request.POST.get('q10')
        try:
            text=Assignments.objects.create(sub=sub,mid="Mid2",q6=q6,q7=q7,q8=q8,q9=q9,q10=q10)
            text.save()
        except:
            text=Assignments.objects.get(sub=sub)
            text.mid="Mid2"
            text.q6=request.POST.get('q6')
            text.q7=request.POST.get('q7')
            text.q8=request.POST.get('q8')
            text.q9=request.POST.get('q9')
            text.q10=request.POST.get('q10')
            text.save()
        messages.success(request,'Success!Assignment Questions has been Posted')
        return render(request,'mid2.html',{'fac':fac,'ans':text,'flag':1})
    ans=Assignments.objects.get(sub=fac.dept)
    ans.mid="Mid2"
    return render(request,'mid2.html',{'fac':fac,'ans':ans,'flag':-1})
def marks(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    students=LoginDetails.objects.filter(usertype="Student")
    if request.method=="POST":
        sub=fac.dept
        for student in students:
            try:
                m1=Mid1.objects.create(username=student.username)
            except:
                m1=Mid1.objects.get(username=student.username)
            try:
                m2=Mid2.objects.create(username=student.username)
            except:
                m2=Mid2.objects.get(username=student.username)
            if sub=="Java_Programming_CSE":
                m1.Java_Programming_Cse=request.POST.get(student.username)
                m2.Java_Programming_Cse=request.POST.get(student.username)
            elif sub=="Data_Structures_Cse":
                m1.Data_Structures_Cse=request.POST.get(student.username)
                m2.Data_Structures_Cse=request.POST.get(student.username)
            elif sub=="Web_Technologies_Cse":
                m1.Web_Technologies_Cse=request.POST.get(student.username)
                m2.Web_Technologies_Cse=request.POST.get(student.username)
            m1.save()
            m2.save()
    return render(request,'marks.html',{'students':students,'sub':fac.dept,'fac':fac})
def logout(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    return render(request,'logout.html',{'uname':uname,'name':name})
def logoutf(request):
    fac=LoginDetails.objects.get(username=request.session.get('uname'))
    uname=request.session.get('uname')
    name=request.session.get('name')
    return render(request,'logoutf.html',{'fac':fac,'uname':uname,'name':name})
def faculty(request):
    fac=LoginDetails.objects.get(username=request.session.get('uname'))
    return render(request,'faculty.html',{'fac':fac})
def admin(request):
    return render(request,'admin.html')
def addusers(request):
    lg=LoginDetails.objects.all()
    return render(request,'addusers.html',{'lg':lg,'adduser':'no'})
def adduserdetails(request):
    lg=LoginDetails.objects.all()
    c=LoginDetails.objects.all().count()
    sub=Mid1.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        usertype=request.POST.get('usertype')
        dept=request.POST.get('dept')
        name=request.POST.get('name')
        newuser=LoginDetails.objects.create(username=username,password=username,name=name,usertype=usertype,dept=dept)
        c=c+1
        newuser.save()
    return render(request,'addusers.html',{'lg':lg,'adduser':'yes','count':c,'sub':sub})
def edituser(request,pk):
    lg=LoginDetails.objects.all()
    c=LoginDetails.objects.all().count()
    sub=Mid1.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        usertype=request.POST.get('usertype')
        dept=request.POST.get('dept')
        name=request.POST.get('name')
        newuser=LoginDetails.objects.create(username=username,password=username,name=name,usertype=usertype,dept=dept)
        newuser.save()
    return render(request,'edituser.html',{'pk':pk,'lg':lg,'adduser':'no','count':c,'sub':sub})
def savechanges(request):
    lg=LoginDetails.objects.all()
    if(request.method=='POST'):
        name=request.POST.get('name')
        username=request.POST.get('username')
        user=LoginDetails.objects.get(username=username)
        user.username=username
        user.name=name
        user.save()
    return render(request,'edituser.html',{'lg':lg})
def deleteuser(request,pk):
    lg=LoginDetails.objects.all()
    c=LoginDetails.objects.all().count()
    sub=Mid1.objects.all()
    LoginDetails.objects.get(username=pk).delete()
    return render(request,'addusers.html',{'lg':lg,'adduser':'yes','count':c,'sub':sub})
