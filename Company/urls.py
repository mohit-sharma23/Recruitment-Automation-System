import imp
from django.shortcuts import render
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from Company import views
from django.conf.urls.static import static

urlpatterns = [
   path('company',views.company_home,name='company'),
   path('company_registration',views.company_registration,name='company_registration'),
   path('add',views.ADD,name='add'),
   path('delete/<int:id>',views.delete,name='delete')
]
