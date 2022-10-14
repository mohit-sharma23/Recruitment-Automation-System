from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from .views import form

urlpatterns = [
    path('',form,name='form'),
]