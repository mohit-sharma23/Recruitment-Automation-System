from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from resume import views

urlpatterns = [
    path('',views.candi_regis,name='candi_regis'),
    path('candihome',views.candihome,name='candihome'),
    path('resume/',views.create_resume,name='create_resume'),
]