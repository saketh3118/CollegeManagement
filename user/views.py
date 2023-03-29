from django.shortcuts import redirect, render
import user
from user.models import LoginDetails,Semester,Attendance,Queries,TimeTable,Assignments
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            lg=LoginDetails.objects.get(username=username)
        except :
            return render(request,'home.html')
        if(lg.username==username and lg.password==password):
            request.session['uname']=lg.username
            request.session['name']=lg.name
            if(lg.usertype=="Faculty"):
                return render(request,'faculty.html')
            return render(request,'index.html',{'lg':lg})
    return render(request,'home.html')
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
    v1=0.0
    v2=0.0
    v3=0.0
    if(temp>=3):
        v1=30
        temp=temp-3
    else:
        v1=temp*10
        temp=0
    if(temp>=4):
        v2=40
        temp=temp-4
    else:
        v2=temp*10
        temp=0
    v3=temp*10
    tt=TimeTable.objects.all()
    assignments=Assignments.objects.all()
    return render(request,'academics.html',{'s':s,'uname':uname,'name':name,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'avg':avg,'tt':tt,'date':tt[0].date.date(),'v1':v1,'v2':v2,'v3':v3,'assignments':assignments})
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
    v1=0.0
    v2=0.0
    v3=0.0
    msg=""
    if(percentage>=65 and percentage<75):
        msg="You're Close to 75% Attendance,Come Regular to Improve"
    elif(percentage>=75):
        msg="Hurray!!You are Elgible for Attending Exams"
    elif(percentage<65):
        msg="You are in Dangerzone Come regular to avoid Detention"
    ans=round(percentage,2)
    if(percentage>=25):
        v1=25
        percentage=percentage-25
    else:
        v1=percentage
        percentage=0
    if(percentage>=40):
        v2=40
        percentage=percentage-40
    else:
        v2=percentage
        percentage=0
    v3=percentage
    return render(request,'attendance.html',{'uname':uname,'name':name,'a':a,'msg':msg,'percentage':ans,'v1':v1,'v2':v2,'v3':v3})
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
    return render(request,'assignments.html')
def mid1(request):
    if request.method=='POST':
        sub=request.POST.get('subject')
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')
        q5=request.POST.get('q5')
        try:
            text=Assignments.objects.create(sub=sub,mid="mid1",q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
        except:
            text=Assignments.objects.get(sub=sub)
        text.save()
    return render(request,'mid1.html')
def mid2(request):
    return render(request,'mid2.html')