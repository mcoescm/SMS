from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    path('find/', views.findstudents, name='findstudents'),
    path('store/', views.store, name='store'),

]