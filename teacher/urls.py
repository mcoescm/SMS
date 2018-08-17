from django.contrib import admin
from django.urls import path
from . import views

app_name="teacher"
urlpatterns = [
    path('',views.index , name='index'),

    path('register/', views.register , name='register'),
    path('update1/', views.update, name='Upadate'),
    path('update/', views.updation, name='Upadate_teacher'),

]
