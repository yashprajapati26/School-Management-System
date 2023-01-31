from itertools import count
from django.shortcuts import render , redirect
from django.core.mail import send_mail
from School_App.models import *

# Create your views here.                                                           

def index(request):
   
    return render(request,"index.html")

def signup(request):
    if request.method == "POST":
        usertype = request.POST['type']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        number = request.POST['number']
        mail = request.POST['mail']
        standard = request.POST['standard']
        file = request.POST['file']
        gender = request.POST['gender']
        password = request.POST['pword']
        cpassword = request.POST['cpword']

        print(usertype)

        try:
            userobj = User.objects.get(mail=mail)
            msg = "You are Already register with this email id"
            context = {'msg':msg}
            return render(request,"login.html",context)
        except: 
            if fname=="" or lname=="" or number =="" or mail=="" or standard =="" or gender == "" or password=="" or cpassword == "": 
                msg="Please enter all details!"
                context = {'msg':msg}
                return render(request,'signup.html',context)
            elif(password == cpassword):
                usertype_obj = UserType.objects.get(user_type=usertype)

                User.objects.create(usertype=usertype_obj , first_name=fname , middle_name=mname , last_name=lname , mobile_no=number , email=mail , standard=standard , photo=file , gender=gender , password=password)

                msg = "You are register sucessfully. please do login."
                return render(request, "login.html",{'msg':msg})
            else:
                msg="password & confirm password does not match"
                return render(request,'signup.html')
    else:
        return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(email=email)
           
            if (password == user.password):
                # session create
                request.session['email'] = email
                request.session['name'] = user.first_name + " " + user.last_name
        
                return redirect("index")
            else:
                msg="Your password does not match"
                context = {'msg':msg}
                print("else block==")

                return render(request,"login.html",context)
        except:
            print("except block==")

            msg = "You are not register with us , first do signup."
            context = {'msg':msg}
            return render(request,"signup.html",context)

        # return render(request,"index.html")
    else:
        return render(request,"login.html")
        

def logout(request):
    del request.session['email']
    del request.session['name']
    return redirect("login")


def teachers(request):
    # user_obj = UserType.objects.get(user_type="Teacher")
    user_obj = UserType.objects.get(user_type="Student")
    teachers= User.objects.filter(usertype=user_obj)
    data = {'teachers' : teachers}
    print(teachers)
    return render(request,"teachers.html",data)

def students(request):
    user_obj = UserType.objects.get(user_type="Student")
    students= User.objects.filter(usertype=user_obj)
    data = {'students' : students}
    return render(request,"students.html",data)

def classes(request):
    return render (request,"classes.html")


def dashboard(request):
    usertype = UserType.objects.get(user_type="Teacher")
    teachers_cnt = User.objects.filter(usertype=usertype).count()
    print(teachers)
    data = {'teachers_cnt':teachers_cnt}
    return render(request,"dashboard.html",data)

def assignment(request):
    if request.method == "POST":

        std = request.POST['standard']
        sub = request.POST['subject']
        ass_file = request.POST['ass_file']

        if(std == "" or sub == "" or ass_file==""):
            msg = "Please Enter All Details."
            data = {'msg':msg}
            return render(request,"assignment.html",data)
        else:
            user = User.objects.get(email=request.session['email'])
            Assignment.objects.create(user=user,subject_name=sub,assignment_file=ass_file)
            msg = "Assignment Upload Sucessfully"
            assignments = Assignment.objects.all()
            data = {'sucess_msg':msg,'assignments':assignments}
            return render(request,"assignment.html",data)

    else:
        assignments = Assignment.objects.all()
        data = {'assignments':assignments}

        return render(request,"assignment.html",data)

def delete_assignment(request,pk):
    print("assignmnet pk : ", pk)
    ass_obj = Assignment.objects.get(pk=pk)
    print(ass_obj)
    ass_obj.delete()
    
    return redirect('assignment')

def update_assignment(request,pk):
    if request.method == "POST":
        assignment = Assignment.objects.get(pk=pk)

        std = request.POST['standard']
        sub = request.POST['subject']
        ass_file = request.POST['ass_file']
        old_file =  request.POST.get('selected_img')

        if ass_file != '':
            assignment.assignment_file = ass_file
        else:
            assignment.assignment_file = old_file
        assignment.subject_name = sub

        assignment.save()
        msg = "Save Changes sucessfully"
        data = {'msg':msg}
        return redirect("assignment")
    else:
        assignment = Assignment.objects.get(pk=pk)
        data = {'assignment':assignment}

        return render(request,"edit_assignment.html",data)


def leave(request):
    if request.method=='POST':

        reason = request.POST['reason']
        start_date = request.POST['start']
        end_date = request.POST['end']
        status = request.POST['status']
       
        if(reason == "" or start_date == "" or end_date==""):
            msg = "Please Enter All Details."
            data = {'msg':msg}
            return render(request,"leave.html",data)

        else:
            user = User.objects.get(email=request.session['email'])
            Leave.objects.create(user=user,reason=reason,start_date=start_date,end_date=end_date)
            msg = "Leave Request Sent Sucessfully"
            leave = Leave.objects.all()
            data = {'sucess_msg':msg,'leave':leave}
            return render(request,"leave.html",data)

    else:
        leave = Leave.objects.all()
        data = {'leave':leave}

        return render(request,"leave.html",data)

def delete_leave(request,pk):
    print("leave pk : ", pk)
    leave_obj = Leave.objects.get(pk=pk)
    print(leave_obj)
    leave_obj.delete()
    
    return redirect('leave')


def update_leave(request,pk):
    if request.method == "POST":
        leave = Leave.objects.get(pk=pk)

        reason = request.POST['reason']
        start_date = request.POST['start']
        end_date = request.POST['end']

        leave.reason = reason
        leave.start_date = start_date
        leave.end_date = end_date
        leave.save() 
        msg = "Save Changes sucessfully"
        data = {'msg':msg}
        return redirect("leave")
    else:
        leave = Leave.objects.get(pk=pk )
        leave = {'leave' :leave}

        return render(request, 'edit_leave.html')
        

def virtual_reality(request):
    return render(request,"virtual-reality.html")

def profile(request):
    return render(request,"profile.html")


def table(request):
    return render(request,"table.html")

def subject(request):
    return render(request,"subject.html")

def forgot_password(request):
    return render(request,"forgot_password.html")

def otp(request):
    return render(request,"otp.html")

def change_password(request):
    return render(request,"change_password.html")
