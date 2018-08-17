from django.contrib import admin
from django.urls import path
from . import views

app_name="teacher"
urlpatterns = [
    path('',views.index , name='index'),
    path('register/', views.register , name='register'),
    path('examschedule/', views.exams , name='exams'),
    path('findsubject/', views.findsubject , name='findsubject'),
    path('schedule/', views.schedule , name='schedule'),
    path('update1/', views.update, name='update_teacher'),
    path('update/', views.updation, name='update'),

]
