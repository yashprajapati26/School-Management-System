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
        mail = request.POST['email']
        standard = request.POST['standard']
        file = request.FILE['file']

        password = request.post['password']
        cpassword = request.post['cpassword']

        try:
            userobj = User.objects.get(email=mail)
            msg = "You are Already register with this email id"
            context = {'msg':msg}
            return render(request,"login.html",context)
        except:        
            if(password == cpassword):
                pass
    else:
        return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        pass
    else:
        return render(request,"login.html")
        
