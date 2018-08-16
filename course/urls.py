from django.contrib import admin
from django.urls import path
from . import views

app_name='course'
urlpatterns = [
    path('',views.index , name='index'),
    path('registercourse/', views.registercourse, name='registercourse'),
    path('updatecourse/', views.updatecourse, name='updatecourse'),
    path('update/', views.update, name='update')

]
