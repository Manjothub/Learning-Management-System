from django.urls import path, include
from Home .views import *

urlpatterns = [
    path('',INDEX,name="homepage"),
    path('about',ABOUTUS,name="about_us"),
    path('course',COURSE_LIST,name="courselist"),
    path('single/course',SINGLE_COURSE,name="single_course"),
    path('contact-us',CONTACT_US,name="contact_us"),
    path('accounts/register',REGISTER,name="register"),
    path('accounts/login',USERLOGIN,name="userlogin"),
    path("logout/", LOGOUT, name="logout"),   
    path("accounts/profile",PROFILE, name="profile"),   
    path("accounts/profile/update",PROFILE_UPDATE, name="profileupdate"),   
]
