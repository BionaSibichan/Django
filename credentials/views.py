from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method=="POST":
        f_name=request.POST['first_name']
        l_name=request.POST['last_name']
        mail=request.POST['email']
        pwd=request.POST['create_password']
        cpwd=request.POST['confirm_password']
        if pwd==cpwd:
            if User.objects.filter(username=mail).exists():
                return HttpResponse("User already exists")
            else:
                user=User.objects.create_user(username=mail,first_name=f_name,last_name=l_name,email=mail,password=pwd)
                user.save()
                return redirect("credentials:Sign_In")
        else:
            return HttpResponse("Passwords must be same kettoo")
    return render(request,"register.html")
def login(request):
    if request.method=="POST":
            mail=request.POST['email']
            pwd=request.POST['password']
            user=auth.authenticate(username=mail,password=pwd)#return None if no value
            if user is not None:
                 auth.login(request,user)
                 return redirect("/")
            else:
                 return HttpResponse("Invalid password or username")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("credentials:Sign_In")
     