from AdminPanel import views
from django.urls import path , include
from django.conf import settings
from django.contrib import admin
urlpatterns=[
    path('',views.check,name='check'),
]