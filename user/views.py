from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib import messages
from user.models import *
from django.db.models import Q
# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['uname']=username
        request.session['name']=username
        user=authenticate(username=username,password=password)
        if(user is not None and username!=''):
            lg=LoginDetails.objects.all()
            return render(request,'addusers.html',{'lg':lg,'adduser':'no','uname':request.session.get('uname'),'name':request.session.get('name')})
        try:
            if(username==''):
                raise Exception
            lg=LoginDetails.objects.get(username=username)
        except:
            messages.success(request,'Invalid Username or Password')
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
def displaytimetable(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    tt=TimeTable.objects.all()
    return render(request,'displaytimetable.html',{'tt':tt,'date':tt[0].date.date(),'assignments':assignments,'uname':uname,'name':name})
def assign(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    assignments=Assignments.objects.all()
    return render(request,'assignmentquestions.html',{'assignments':assignments,'uname':uname,'name':name})
def mid(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    m1=Mid1.objects.get(username=uname)
    m2=Mid2.objects.get(username=uname)
    return render(request,'midmarks.html',{'m1':m1,'m2':m2,'uname':uname,'name':name})
def semresults(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    s=Semester.objects.get(username=uname)
    sum1=0.0
    l=[s.c1,s.c2,s.c3,s.c4,s.c5,s.c6,s.c7,s.c8]
    TotalCredits=21
    j=0
    for i in [s.LANM,s.EC,s.BEEE,s.PPS,s.PPS_LAB,s.EC_LAB,s.BEEE_LAB,s.IT_WORKSHOP]:
        sum1=sum1+(i*float(l[j]))
        j=j+1
    sum1=sum1/TotalCredits
    sum1=round(sum1,2)
    sum2=0.0
    l=[s.c9,s.c10,s.c11,s.c12,s.c13,s.c14,s.c15,s.c16]
    j=0
    TotalCredits=21
    for i in [s.ENG,s.PandS,s.SCP,s.PYTHON,s.EG,s.ENG_LAB,s.SCP_LAB,s.PYTHON_LAB]:
        sum2=sum2+i*float(l[j])
        j=j+1
    sum2=sum2/TotalCredits
    sum2=round(sum2,2)
    sum3=0.0
    l=[s.c17,s.c18,s.c19,s.c20,s.c21,s.c22,s.c23,s.c24,s.c25]
    j=0
    TotalCredits=20
    for i in [s.DM,s.COA,s.DS,s.JAVA,s.OS,s.DS_LAB,s.JAVA_LAB,s.OS_LAB,s.GS]:
        sum3=sum3+i*float(l[j])
        j=j+1
    sum3=sum3/TotalCredits
    sum3=round(sum3,2)
    sum4=0.0
    l=[s.c26,s.c27,s.c28,s.c29,s.c30,s.c31,s.c32,s.c33,s.c34]
    j=0
    TotalCredits=20
    for i in [s.ASOT,s.DBMS,s.WT,s.DAA,s.CC,s.DBMS_LAB,s.WT_LAB,s.DAA_LAB,s.ES]:
        sum4=sum4+i*float(l[j])
        j=j+1
    sum4=sum4/TotalCredits
    sum4=round(sum4,2)
    avg=round((sum1+sum2+sum3+sum4)/4,2)
    temp=avg
    v1=temp*10
    return render(request,'semresults.html',{'s':s,'uname':uname,'name':name,'sum1':sum1,'sum2':sum2,'sum3':sum3,'sum4':sum4,'avg':avg,'avg1':sum1,'avg2':round((sum1+sum2)/2,2),'avg3':round((sum1+sum2+sum3)/3,2),'avg4':round((sum1+sum2+sum3+sum4)/4,2),'v1':v1,'assignments':assignments})
def attendance(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    a=TotalAttendance.objects.get(Dept="CSE")
    b=Attendance.objects.get(username=uname)
    sum1=0.0
    sum2=0.0
    for i in [b.DM,b.CNS,b.EEA,b.GB,b.CD,b.QA,b.DM_LAB,b.CD_LAB,b.ENG_LAB]:
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
    return render(request,'attendance.html',{'uname':uname,'name':name,'a':a,'b':b,'msg':msg,'percentage':ans,'v1':ans})
def contactus(request):
    uname=request.session.get('uname')
    name=request.session.get('name')
    det=LoginDetails.objects.filter(usertype="Faculty")
    # if request.method=='POST':
    #     uname=request.session.get('uname')
    #     name=request.session.get('name')
    #     sel=request.POST.get('dropdown')
    #     return render(request,'send_message.html',{'selected':sel,'users':det,'uname':uname,'name':name})
    return render(request,'contactus.html',{'selected':'','users':det,'uname':uname,'name':name})
def send_message(request,pk):
    uname=request.session.get('uname')
    name=request.session.get('name')
    selctedname=LoginDetails.objects.get(username=pk).name
    selcteddept=LoginDetails.objects.get(username=pk).dept
    messagelist=Message.objects.filter((Q(sender=uname) & Q(receiver=pk)) | (Q(sender=pk) & Q(receiver=uname)))
    return render(request,'send_message.html',{'selected':pk,'selecteddept':selcteddept,'selectedname':selctedname,'uname':uname,'name':name,'messagelist':messagelist})
def message_sent(request,pk):
    uname=request.session.get('uname')
    name=request.session.get('name')
    sender=LoginDetails.objects.get(username=uname)
    selctedname=LoginDetails.objects.get(username=pk).name
    selcteddept=LoginDetails.objects.get(username=pk).dept
    messagelist=Message.objects.filter((Q(sender=uname) & Q(receiver=pk)) | (Q(sender=pk) & Q(receiver=uname)))
    if request.method=='POST':
        if request.POST.get('text')=='':
            messages.warning(request,"Message Can't be Empty")
        else:
            message_id=Message.objects.filter().count()+1
            object=Message.objects.create(message_id=message_id)
            object.sender=sender.username
            object.receiver=pk
            object.message=request.POST.get('text')
            object.save()
            messagelist=Message.objects.filter((Q(sender=uname) & Q(receiver=pk)) | (Q(sender=pk) & Q(receiver=uname)))
    return render(request,'send_message.html',{'selected':pk,'selecteddept':selcteddept,'selectedname':selctedname,'uname':uname,'name':name,'messagelist':messagelist})
def contact_students(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    det=LoginDetails.objects.filter(usertype="Student")
    return render(request,'contact_students.html',{'users':det,'fac':fac,'uname':fac.username,'name':fac.name})
def send_message_faculty(request,pk):
    uname=request.session.get('uname')
    name=request.session.get('name')
    fac=LoginDetails.objects.get(username=uname)
    selectedname=LoginDetails.objects.get(username=pk).name
    selecteddept=LoginDetails.objects.get(username=pk).dept
    messagelist=Message.objects.filter((Q(sender=uname) & Q(receiver=pk)) | (Q(sender=pk) & Q(receiver=uname)))
    return render(request,'send_message_faculty.html',{'selected':pk,'selecteddept':selecteddept,'selectedname':selectedname,'uname':uname,'fac':fac,'name':name,'messagelist':messagelist})
def message_sent_faculty(request,pk):
    uname=request.session.get('uname')
    name=request.session.get('name')
    sender=LoginDetails.objects.get(username=uname)
    selctedname=LoginDetails.objects.get(username=pk).name
    selcteddept=LoginDetails.objects.get(username=pk).dept
    messagelist=Message.objects.filter((Q(sender=uname) & Q(receiver=pk)) | (Q(sender=pk) & Q(receiver=uname)))
    if request.method=='POST':
        if request.POST.get('text')=='':
            messages.warning(request,"Message Can't be Empty")
        else:
            message_id=Message.objects.filter().count()+1
            object=Message.objects.create(message_id=message_id)
            object.sender=sender.username
            object.receiver=pk
            object.message=request.POST.get('text')
            object.save()
            messagelist=Message.objects.filter((Q(sender=uname) & Q(receiver=pk)) | (Q(sender=pk) & Q(receiver=uname)))
    return render(request,'send_message_faculty.html',{'selected':pk,'selecteddept':selcteddept,'selectedname':selctedname,'uname':uname,'fac':sender,'name':name,'messagelist':messagelist})
def assignments(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    return render(request,'assignments.html',{'fac':fac})
def mid1(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    sub=fac.dept
    try:
        ans=Assignments.objects.get(sub=sub)
        ans.mid="Mid1"
    except:
        ans=Assignments.objects.create(sub=sub,mid="Mid1")
    ans.save()
    if request.method=='POST':
        text=Assignments.objects.get(sub=sub)
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')
        q5=request.POST.get('q5')
        text.mid="Mid1"
        text.q1=q1
        text.q2=q2
        text.q3=q3
        text.q4=q4
        text.q5=q5
        text.save()
        messages.success(request,'Success!Assignment Questions has been Posted')
        return render(request,'mid1.html',{'fac':fac,'ans':text,'flag':1})
    return render(request,'mid1.html',{'fac':fac,'ans':ans,'flag':-1})
def mid2(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    sub=fac.dept
    try:
        ans=Assignments.objects.get(sub=sub)
        ans.mid="Mid2"
    except:
        ans=Assignments.objects.create(sub=sub,mid="Mid2")
    ans.save()
    if request.method=='POST':
        text=Assignments.objects.get(sub=sub)
        sub=fac.dept
        q6=request.POST.get('q6')
        q7=request.POST.get('q7')
        q8=request.POST.get('q8')
        q9=request.POST.get('q9')
        q10=request.POST.get('q10')
        text.mid="Mid2"
        text.q6=q6
        text.q7=q7
        text.q8=q8
        text.q9=q9
        text.q10=q10
        text.save()
        messages.success(request,'Success!Assignment Questions has been Posted')
        return render(request,'mid2.html',{'fac':fac,'ans':text,'flag':1})
    return render(request,'mid2.html',{'fac':fac,'ans':ans,'flag':-1})
def marks(request):
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    # students=LoginDetails.objects.filter(usertype="Student").order_by('username')
    # M1=Mid1.objects.all().order_by('username')
    # M2=Mid2.objects.all().order_by('username')
    # if request.method=="POST":
    #     sub=fac.dept
    #     for student in students:
    #         try:
    #             m1=Mid1.objects.create(username=student.username,name=student.name)
    #         except:
    #             m1=Mid1.objects.get(username=student.username)
    #         try:
    #             m2=Mid2.objects.create(username=student.username,name=student.name)
    #         except:
    #             m2=Mid2.objects.get(name=student.name)
    #         if sub=="Java_Programming_Cse":
    #             m1.Java_Programming_Cse=request.POST.get(student.username)
    #             m2.Java_Programming_Cse=request.POST.get(student.name)
    #             # M1=Mid1.objects.values_list('username','name','Java_Programming_Cse')
    #         elif sub=="Data_Structures_Cse":
    #             m1.Data_Structures_Cse=request.POST.get(student.username)
    #             m2.Data_Structures_Cse=request.POST.get(student.name)
    #             # M1=Mid1.objects.values_list('username','name','Data_Structures_Cse')
    #         elif sub=="Web_Technologies_Cse":
    #             m1.Web_Technologies_Cse=request.POST.get(student.username)
    #             m2.Web_Technologies_Cse=request.POST.get(student.name)
    #             # M1=Mid1.objects.values_list('username','name','Web_Technologies_Cse')
    #         m1.save()
    #         m2.save()
    return render(request,'marks.html',{'sub':fac.dept,'fac':fac})
def midmarks1(request):
    stu=LoginDetails.objects.filter(usertype="Student")
    for s in stu:
        try:
            Mid1.objects.create(name=s.name,username=s.username)
        except:
            Mid1.objects.get(name=s.name)
    students=Mid1.objects.all().order_by('username')
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    sub=fac.dept
    if request.method=="POST":
        for student in students:
            try:
                m1=Mid1.objects.create(username=student.username,name=student.name)
            except:
                m1=Mid1.objects.get(username=student.username)
            if sub=="Java_Programming_Cse":
                m1.Java_Programming_Cse=request.POST.get(student.username)
            elif sub=="Data_Structures_Cse":
                m1.Data_Structures_Cse=request.POST.get(student.username)
            elif sub=="Web_Technologies_Cse":
                m1.Web_Technologies_Cse=request.POST.get(student.username)
            m1.save()
        students=Mid1.objects.all().order_by('username')
        return render(request,'midmarks1.html',{'students':students,'sub':fac.dept,'fac':fac})
    return render(request,'midmarks1.html',{'students':students,'sub':fac.dept,'fac':fac})
def midmarks2(request):
    stu=LoginDetails.objects.filter(usertype="Student")
    for s in stu:
        try:
            Mid2.objects.create(name=s.name,username=s.username)
        except:
            Mid2.objects.get(name=s.name)
    students=Mid2.objects.all().order_by('username')
    uname=request.session.get('uname')
    fac=LoginDetails.objects.get(username=uname)
    sub=fac.dept
    if request.method=="POST":
        for student in students:
            try:
                m2=Mid2.objects.create(username=student.username,name=student.name)
            except:
                m2=Mid2.objects.get(name=student.name)
            if sub=="Java_Programming_Cse":
                m2.Java_Programming_Cse=request.POST.get(student.name)
            elif sub=="Data_Structures_Cse":
                m2.Data_Structures_Cse=request.POST.get(student.name)
            elif sub=="Web_Technologies_Cse":
                m2.Web_Technologies_Cse=request.POST.get(student.name)
            m2.save()
        students=Mid2.objects.all().order_by('username')
        return render(request,'midmarks2.html',{'students':students,'sub':fac.dept,'fac':fac})
    return render(request,'midmarks2.html',{'students':students,'sub':fac.dept,'fac':fac})
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
    # ad=LoginDetails.objects.get(username=request.session.get('uname'))
    lg=LoginDetails.objects.all()
    return render(request,'addusers.html',{'lg':lg,'adduser':'no','uname':request.session.get('uname'),'name':request.session.get('name')})
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
        newuser.save()
        messages.success(request,'Success!User Details has been Added')
        return render(request,'addusers.html',{'lg':lg,'adduser':'no','count':c,'sub':sub,'uname':request.session.get('uname'),'name':request.session.get('name')})
    return render(request,'addusers.html',{'lg':lg,'adduser':'yes','count':c,'sub':sub,'uname':request.session.get('uname'),'name':request.session.get('name')})
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
    return render(request,'edituser.html',{'pk':pk,'lg':lg,'adduser':'no','count':c,'sub':sub,'uname':request.session.get('uname'),'name':request.session.get('name')})
def savechanges(request):
    lg=LoginDetails.objects.all()
    if(request.method=='POST'):
        name=request.POST.get('name')
        username=request.POST.get('username')
        usertype=request.POST.get('usertype')
        dept=request.POST.get('dept')
        user=LoginDetails.objects.get(username=username)
        user.username=username
        user.name=name
        user.dept=dept
        user.usertype=usertype
        user.save()
        messages.success(request,'Success!User Details has edited Successfully')
    return render(request,'addusers.html',{'lg':lg,'uname':request.session.get('uname'),'name':request.session.get('name')})
def deleteuser(request,pk):
    lg=LoginDetails.objects.all()
    c=LoginDetails.objects.all().count()
    sub=Mid1.objects.all()
    LoginDetails.objects.get(username=pk).delete()
    messages.success(request,'Success!User Details has Deleted')
    return render(request,'addusers.html',{'lg':lg,'adduser':'no','count':c,'sub':sub,'uname':request.session.get('uname'),'name':request.session.get('name')})
def listofsems(request):
    return render(request,'listOfSems.html',{'uname':request.session.get('uname'),'name':request.session.get('name')})
# def editresults(request,pk):
#     student=LoginDetails.objects.get(username=pk)
#     return render(request,'editresults.html',{'user':student})
def edituserresults(request,pk,sem):
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    stu=LoginDetails.objects.get(username=pk)
    if sem=="sem1":
        try:
            student=Semester.objects.get(username=pk)
        except:
            student=Semester.objects.create(username=stu,LANM=0,EC=0,BEEE=0,PPS=0,PPS_LAB=0,EC_LAB=0,BEEE_LAB=0,IT_WORKSHOP=0,c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0)
        if request.method=="POST":
            student.LANM=request.POST.get('lanm')
            student.c1=request.POST.get('lanm_credits')
            student.EC=request.POST.get('ec')
            student.c2=request.POST.get('ec_credits')
            student.BEEE=request.POST.get('beee')
            student.c3=request.POST.get('beee_credits')
            student.PPS=request.POST.get('pps')
            student.c4=request.POST.get('pps_credits')
            student.PPS_LAB=request.POST.get('pps_lab')
            student.c5=request.POST.get('pps_lab_credits')
            student.EC_LAB=request.POST.get('ec_lab')
            student.c6=request.POST.get('ec_lab_credits')
            student.BEEE_LAB=request.POST.get('beee_lab')
            student.c7=request.POST.get('beee_lab_credits')
            student.IT_WORKSHOP=request.POST.get('it')
            student.c8=request.POST.get('it_credits')
            student.save()
            messages.success(request,'Success! '+stu.username+' Semester I Results has Updated')
    elif sem=="sem2":
        try:
            student=Semester.objects.get(username=pk)
        except:
            student=Semester.objects.create(username=stu,ENG=0,PandS=0,SCP=0,PYTHON=0,EG=0,ENG_LAB=0,SCP_LAB=0,PYTHON_LAB=0,c9=0,c10=0,c11=0,c12=0,c13=0,c14=0,c15=0,c16=0)
        if request.method=="POST":
            student.ENG=request.POST.get('eng')
            student.c9=request.POST.get('eng_credits')
            student.PandS=request.POST.get('pands')
            student.c10=request.POST.get('pands_credits')
            student.SCP=request.POST.get('scp')
            student.c11=request.POST.get('scp_credits')
            student.PYTHON=request.POST.get('python')
            student.c12=request.POST.get('python_credits')
            student.EG=request.POST.get('eg')
            student.c13=request.POST.get('eg_credits')
            student.ENG_LAB=request.POST.get('eng_lab')
            student.c14=request.POST.get('eng_lab_credits')
            student.SCP_LAB=request.POST.get('scp_lab')
            student.c15=request.POST.get('scp_lab_credits')
            student.PYTHON_LAB=request.POST.get('python_lab')
            student.c16=request.POST.get('python_lab_credits')
            student.save()
            messages.success(request,'Success! '+stu.username+' Semester II Results has Updated')
    elif sem=="sem3":
        try:
            student=Semester.objects.get(username=pk)
        except:
            student=Semester.objects.create(username=stu,DM=0,COA=0,DS=0,JAVA=0,OS=0,DS_LAB=0,JAVA_LAB=0,OS_LAB=0,GS=0,c17=0,c18=0,c19=0,c20=0,c21=0,c22=0,c23=0,c24=0,c25=0)
        if request.method=="POST":
            student.DM=request.POST.get('dm')
            student.c17=request.POST.get('dm_credits')
            student.COA=request.POST.get('coa')
            student.c18=request.POST.get('coa_credits')
            student.DS=request.POST.get('ds')
            student.c19=request.POST.get('ds_credits')
            student.JAVA=request.POST.get('java')
            student.c20=request.POST.get('java_credits')
            student.OS=request.POST.get('os')
            student.c21=request.POST.get('os_credits')
            student.DS_LAB=request.POST.get('ds_lab')
            student.c22=request.POST.get('ds_lab_credits')
            student.JAVA_LAB=request.POST.get('java_lab')
            student.c23=request.POST.get('java_lab_credits')
            student.OS_LAB=request.POST.get('os_lab')
            student.c24=request.POST.get('os_lab_credits')
            student.GS=request.POST.get('gs')
            student.c25=request.POST.get('gs_credits')
            student.save()
            messages.success(request,'Success! '+stu.username+' Semester III Results has Updated')
    elif sem=="sem4":
        try:
            student=Semester.objects.get(username=pk)
        except:
            student=Semester.objects.create(username=stu,ASOT=0,DBMS=0,WT=0,DAA=0,CC=0,DBMS_LAB=0,WT_LAB=0,DAA_LAB=0,ES=0,c26=0,c27=0,c28=0,c29=0,c30=0,c31=0,c32=0,c33=0,c34=0)
        if request.method=="POST":
            student.ASOT=request.POST.get('asot')
            student.c26=request.POST.get('asot_credits')
            student.DBMS=request.POST.get('dbms')
            student.c27=request.POST.get('dbms_credits')
            student.WT=request.POST.get('wt')
            student.c28=request.POST.get('wt_credits')
            student.DAA=request.POST.get('daa')
            student.c29=request.POST.get('daa_credits')
            student.CC=request.POST.get('cc')
            student.c30=request.POST.get('cc_credits')
            student.DBMS_LAB=request.POST.get('dbms_lab')
            student.c31=request.POST.get('dbms_lab_credits')
            student.WT_LAB=request.POST.get('wt_lab')
            student.c32=request.POST.get('wt_lab_credits')
            student.DAA_LAB=request.POST.get('daa_lab')
            student.c33=request.POST.get('daa_lab_credits')
            student.ES=request.POST.get('es')
            student.c34=request.POST.get('es_credits')
            student.save()
            messages.success(request,'Success! '+stu.username+' Semester IV Results has Updated')
    return render(request,'editresults.html',{'stu':stu,'username':pk,'sem':sem,'users':users,'student':student,'uname':request.session.get('uname'),'name':request.session.get('name')})
def sem1(request):
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    subjects=[["LANM",4],["EC",4],["BEEE",3],["PPS",3],["PPS_LAB",3],["BEE_LAB",1.5],["EC_LAB",1],["IT_WORKSHOP",1.5]]
    return render(request,'sem.html',{'users':users,'sem':'sem1','subjects':subjects,'uname':request.session.get('uname'),'name':request.session.get('name')})
def sem2(request):
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    subjects=[["ENG",3],["PandS",3],["SCP",4],["PYTHON",4],["EG",3],["ENG_LAB",1],["SCP_LAB",1],["PYTHON_LAB",2]]
    return render(request,'sem.html',{'users':users,'sem':'sem2','subjects':subjects,'uname':request.session.get('uname'),'name':request.session.get('name')})
def sem3(request):
    subjects=[["DM",3],["COA",3],["DS",3],["JAVA",3],["OS",3],["DS_LAB",1.5],["JAVA_LAB",1.5],["OS_LAB",2],["GS",0]]
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    return render(request,'sem.html',{'users':users,'sem':'sem3','subjects':subjects,'uname':request.session.get('uname'),'name':request.session.get('name')})
def sem4(request):
    subjects=[["ASOT",3],["DBMS",3],["WT",3],["DAA",3],["CC",3],["DBMS LAB",2],["WT LAB",1.5],["DAA LAB",1.5],["ES",0]]
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    return render(request,'sem.html',{'users':users,'sem':'sem4','subjects':subjects,'uname':request.session.get('uname'),'name':request.session.get('name')})
def timetable(request):
    try:
        d1=TimeTable.objects.get(Day="MONDAY")
    except:
        d1=TimeTable.objects.create(Day="MONDAY",Year=3)
    try:
        d2=TimeTable.objects.get(Day="TUESDAY")
    except:
        d2=TimeTable.objects.create(Day="TUESDAY",Year=3)
    try:
        d3=TimeTable.objects.get(Day="WEDNESDAY")
    except:
        d3=TimeTable.objects.create(Day="WEDNESDAY",Year=3)
    try:
        d4=TimeTable.objects.get(Day="THURSDAY")
    except:
        d4=TimeTable.objects.create(Day="THURSDAY",Year=3)
    try:
        d5=TimeTable.objects.get(Day="FRIDAY")
    except:
        d5=TimeTable.objects.create(Day="FRIDAY",Year=3)
    try:
        d6=TimeTable.objects.get(Day="SATURDAY")
    except:
        d6=TimeTable.objects.create(Day="SATURDAY",Year=3)
    if request.method=="POST":
            d1.C1=request.POST.get('mc1')
            d1.C2=request.POST.get('mc2')
            d1.C3=request.POST.get('mc3')
            d1.C4=request.POST.get('mc4')
            d1.C5=request.POST.get('mc5')
            d1.C6=request.POST.get('mc6')
            d1.C7=request.POST.get('mc7')
            d1.date=timezone.now()
            d1.Dept='CSE'
            d1.Year=3
            d1.save()
            d2.C1=request.POST.get('tc1')
            d2.C2=request.POST.get('tc2')
            d2.C3=request.POST.get('tc3')
            d2.C4=request.POST.get('tc4')
            d2.C5=request.POST.get('tc5')
            d2.C6=request.POST.get('tc6')
            d2.C7=request.POST.get('tc7')
            d2.date=timezone.now()
            d2.Dept="CSE"
            d2.Year=3
            d2.save()
            d3.C1=request.POST.get('wc1')
            d3.C2=request.POST.get('wc2')
            d3.C3=request.POST.get('wc3')
            d3.C4=request.POST.get('wc4')
            d3.C5=request.POST.get('wc5')
            d3.C6=request.POST.get('wc6')
            d3.C7=request.POST.get('wc7')
            d3.date=timezone.now()
            d3.Dept="CSE"
            d3.Year=3
            d3.save()
            d4.C1=request.POST.get('thc1')
            d4.C2=request.POST.get('thc2')
            d4.C3=request.POST.get('thc3')
            d4.C4=request.POST.get('thc4')
            d4.C5=request.POST.get('thc5')
            d4.C6=request.POST.get('thc6')
            d4.C7=request.POST.get('thc7')
            d4.date=timezone.now()
            d4.Dept="CSE"
            d4.Year=3
            d4.save()
            d5.C1=request.POST.get('fc1')
            d5.C2=request.POST.get('fc2')
            d5.C3=request.POST.get('fc3')
            d5.C4=request.POST.get('fc4')
            d5.C5=request.POST.get('fc5')
            d5.C6=request.POST.get('fc6')
            d5.C7=request.POST.get('fc7')
            d5.date=timezone.now()
            d5.Dept="CSE"
            d5.Year=3
            d5.save()
            d6.C1=request.POST.get('sc1')
            d6.C2=request.POST.get('sc2')
            d6.C3=request.POST.get('sc3')
            d6.C4=request.POST.get('sc4')
            d6.C5=request.POST.get('sc5')
            d6.C6=request.POST.get('sc6')
            d6.C7=request.POST.get('sc7')
            d6.date=timezone.now()
            d6.Dept="CSE"
            d6.Year=3
            d6.save()
            messages.success(request,'Success! Time Table has been Updated')
            return render(request,'timetable.html',{'d1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'uname':request.session.get('uname'),'name':request.session.get('name')})
    return render(request,'timetable.html',{'d1':d1,'d2':d2,'d3':d3,'d4':d4,'d5':d5,'d6':d6,'uname':request.session.get('uname'),'name':request.session.get('name')})
def editattendance(request):
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    try:
        attendance=TotalAttendance.objects.get(Dept="CSE")
    except:
        attendance=TotalAttendance.objects.create(Dept="CSE")
    subjects=['DM','CNS','EEA','GB','CD','QA','DM LAB','CD LAB','ENG LAB']
    if request.method=="POST":
        dm=int(request.POST.get('dm'))
        cns=int(request.POST.get('cns'))
        eea=int(request.POST.get('eea'))
        gb=int(request.POST.get('gb'))
        cd=int(request.POST.get('cd'))
        qa=int(request.POST.get('qa'))
        dm_lab=int(request.POST.get('dm_lab'))
        cd_lab=int(request.POST.get('cd_lab'))
        eng_lab=int(request.POST.get('eng_lab'))
        attendance.DM_TOTAL=dm
        attendance.CNS_TOTAL=cns
        attendance.EEA_TOTAL=eea
        attendance.GB_TOTAL=gb
        attendance.CD_TOTAL=cd
        attendance.QA_TOTAL=qa
        attendance.DM_LAB_TOTAL=dm_lab
        attendance.CD_LAB_TOTAL=cd_lab
        attendance.ENG_LAB_TOTAL=eng_lab
        attendance.save()
        messages.success(request,'Success! Total Number of Classes has been Updated')
    return render(request,'edit_attendance.html',{'users':users,'subjects':subjects,'attendance':attendance,'uname':request.session.get('uname'),'name':request.session.get('name')})
def edituserattendance(request,pk):
    users=LoginDetails.objects.filter(usertype="Student").order_by('username')
    total=TotalAttendance.objects.get(Dept="CSE")
    user=LoginDetails.objects.get(username=pk)
    try:
        attendance=Attendance.objects.get(username=user)
    except:
        attendance=Attendance.objects.create(username=user)
    if request.method=="POST":
        dm=int(request.POST.get('dm'))
        cns=int(request.POST.get('cns'))
        eea=int(request.POST.get('eea'))
        gb=int(request.POST.get('gb'))
        cd=int(request.POST.get('cd'))
        qa=int(request.POST.get('qa'))
        dm_lab=int(request.POST.get('dm_lab'))
        cd_lab=int(request.POST.get('cd_lab'))
        eng_lab=int(request.POST.get('eng_lab'))
        attendance.DM=dm
        attendance.CNS=cns
        attendance.EEA=eea
        attendance.GB=gb
        attendance.CD=cd
        attendance.QA=qa
        attendance.DM_LAB=dm_lab
        attendance.CD_LAB=cd_lab
        attendance.ENG_LAB=eng_lab
        attendance.save()
        messages.success(request,'Success! '+user.username+' Attendance has been Updated')
    return render(request,'edituserattendance.html',{'stu':user,'pk':pk,'users':users,'attendance':attendance,'total':total,'uname':request.session.get('uname'),'name':request.session.get('name')})
def logoutadmin(request):
    return render(request,'logoutadmin.html')