from django.urls import path,include

from . import views
app_name="student"

urlpatterns = [
    path('', views.studreg, name='student_register'),
    path('stud_save/', views.studsave, name='Student_save'),
    ]

