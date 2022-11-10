from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from .views import form,can_exam

urlpatterns = [
    # path('',form,name='form'),
    path('can-exam',can_exam,name='can-exam'),
]