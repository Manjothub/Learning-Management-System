from django.urls import path, include
from Home .views import *

urlpatterns = [
    path('',INDEX,name="homepage"),
    path('about',ABOUTUS,name="about"),
    path('single/course',SINGLE_COURSE,name="single_course")
]
