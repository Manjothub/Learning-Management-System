from django.shortcuts import render, redirect

def INDEX(request):
    return render(request,'user/index.html')

def ABOUTUS(request):
    return render(request, 'user/about.html')

def SINGLE_COURSE(request):
    return render(request, 'user/single_course.html')
