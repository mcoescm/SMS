from django.contrib import admin
from django.urls import path
from . import views
app_name="subject"
urlpatterns = [
    path('',views.index , name='index'),
    path('register_subject/',views.register , name='register')

]
