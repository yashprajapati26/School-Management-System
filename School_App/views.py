from django.shortcuts import render , redirect
from django.core.mail import send_mail
from School_App.models import User,UserType

# Create your views here.

def index(request):
    return render(request,"index.html")

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