from django.contrib import admin
from django.urls import path
from . import views

app_name="teacher"
urlpatterns = [
    path('',views.index , name='index'),
    path('register/', views.register , name='register'),
    path('examschedule/', views.examschedule , name='examschedule'),
    path('findsubject/', views.findsubject , name='findsubject'),
    path('schedule/', views.schedule , name='schedule'),



]
