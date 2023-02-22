from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib import messages

def index(req):
    return render(req,"main/index.html")
# Create your views here.


# 유저 로그인

def signin_user(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un,password=up)
        if u:
            login(req,u)
            messages.success(req,f"{u} Welcome My Site")
            return redirect("main:index")
        else:
            messages.error(req,"계정 정보를 확인해 주세요")
    return render(req,"main/signin.html")

def signout_user(req):
    logout(req)
    return redirect("main:index")

def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        up1 = req.POST.get("upass1")
        uc = req.POST.get("ucomn")
        pi = req.FILES.get("upic")
        if up != up1:
            messages.error(req,"Passoword가 일치하지 않습니다")
            return redirect("main:signup")
        else:  
            User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
            return redirect("main:signin")
    return render(req,"main/signup.html")


def profile(req):
    return render(req, "main/profile.html")

def delete(req):
    req.user.delete()
    return redirect("main:index")

def update(req):
    if req.method == "POST":
        u = req.user
        up = req.POST.get("upass")
        um = req.POST.get("umail")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucomn")       
        if up:
            u.set_password(up)
        if pi:
            u.pic = pi
        u.comment = uc
        u.email = um
        u.save()
        login(req,u)
        return redirect("main:profile")
    return render(req,"main/update.html")