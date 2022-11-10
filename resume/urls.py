from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from resume import views

urlpatterns = [
    path('create_resume/',views.create_resume),
]