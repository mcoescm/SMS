from . import views
from django.urls import path


app_name = 'login'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('checklogin/', views.checklogin, name="checklogin")
    ]