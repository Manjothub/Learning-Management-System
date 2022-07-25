from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from Home.EmailBacken import EmailBackend
from django.contrib.auth import authenticate,login,logout
from Home.models import *

def INDEX(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    context = {
        'category':category,
        'course':course,
    }

    return render(request,'user/index.html',context)

def ABOUTUS(request):
    return render(request, 'user/about.html')

def SINGLE_COURSE(request):
    return render(request, 'user/single_course.html')

def COURSE_LIST(request):
    category = Categories.get_all_category(Categories)
    level= Level.objects.all()
    course = Course.objects.all()
    context ={
        'category':category,
        'level':level,
        'courses':course
    }
    return render(request,'user/course_list.html',context)

def COURSE_SINGLE(request):
    return render(request,'user/single_course.html')

def CONTACT_US(request):
    return render(request,'user/contact_us.html')

def REGISTER(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('password')
        
        #check email
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists')
            return redirect('register')
        
        #check username
        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('register')
        user = User(
        username=username,
        email = email,
        )
        user.set_password(password)
        user.save()
        return redirect('userlogin')

    return render(request,'user/register.html')


def USERLOGIN(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request,username=email,password=password)
        if user !=None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('userlogin')
    return render(request,'user/login.html')

def PROFILE(request):
    return render(request,'registeration/profile.html')

def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id
        
        
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')
    return 











def LOGOUT(request):
    logout(request)
    return redirect ("/")