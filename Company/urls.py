import imp
from django.shortcuts import render
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from Company import views
from .views import JobDetailView
from django.conf.urls.static import static


urlpatterns = [
   path('',views.company_home,name='company'),
   path('company_registration',views.company_registration,name='company_registration'),
   path('comphome/',views.companyhome,name='comphome'),
   path('comphome/add',views.ADD,name='add'),
   path('jobinfo/',views.job_info,name='jobinfo'),
   path('delete/<int:id>/',views.delete,name='delete'),
   path('jobroles/<int:pk>/', JobDetailView.as_view(template_name='views.html'), name='job_details'),
   path('disresume/',views.disresume,name='disresume'),
   path('accept/',views.accept,name='accept'),
   path('deltest/<int:id>/',views.deltest,name='deltest')
]
