import imp
from django.shortcuts import render
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from Company import views
from .views import JobDetailView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('company/',views.company_home,name='company'),
   path('company/company_registration',views.company_registration,name='company_registration'),
   path('login/',auth_views.LoginView.as_view(template_name='company.html'),name='login'),
   path('comphome/',views.companyhome,name='comphome'),
   path('comphome/add',views.ADD,name='add'),
   path('jobinfo/',views.job_info,name='jobinfo'),
   path('delete/<int:id>/',views.delete,name='delete'),
   path('jobroles/<int:pk>/', JobDetailView.as_view(template_name='views.html'), name='job_details'),
]
