from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from Company import views
from django.conf.urls.static import static

urlpatterns = [
   path('company',views.company_home,name='company'),
   path('company_registration',views.company_registration,name='company_registration'),
]
