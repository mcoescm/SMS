from django.contrib import admin
from django.urls import path,include
from . import views
app_name="parent"
urlpatterns = [
    path('', views.index , name='index'),
    path('register/', views.register , name='register'),


]