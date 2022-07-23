from django.shortcuts import render, redirect

def INDEX(request):
    return render(request,'user/index.html')

def ABOUTUS(request):
    return render(request, 'user/about.html')

def SINGLE_COURSE(request):
    return render(request, 'user/single_course.html')

def COURSE_LIST(request):
    return render(request,'user/course_list.html')

def COURSE_SINGLE(request):
    return render(request,'user/single_course.html')

def CONTACT_US(request):
    return render(request,'user/contact_us.html')
