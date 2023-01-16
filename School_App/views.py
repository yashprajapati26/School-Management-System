from django.shortcuts import render
from django.core.mail import send_mail
from School_App.models import User,UserType

# Create your views here.

def signup(request):
    if request.method == "POST":
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
                return render(request, "login.html")
            else:
                msg="password & confirm password does not match"
                return render(request,'signup.html')
    else:
        return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST["mail_id"]
        password = request.POST["pass"]
        return render(request,"index.html")
    else:
        return render(request,"login.html")
        


def index(request):
    if request.method == "POST":
        return render(request="index.html")
    else:
        return render(request="login.html")