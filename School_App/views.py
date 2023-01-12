from django.shortcuts import render

# Create your views here.

def signup(request):
    if request.method == "POST":
        fname = request.post['fname']
        mname = request.post['mname']
        password = request.post['password']
        cpassword = request.post['cpassword']
        if(password == cpassword):
            pass
    else:
        return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        pass
    else:
        return render(request,"login.html")
        
