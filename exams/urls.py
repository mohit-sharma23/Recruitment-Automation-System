from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from .views import form,can_exam,exam_res

urlpatterns = [
    path('form/<int:id>/',form,name='form'),
    path('can-exam/<int:id>/',can_exam,name='can-exam'),
    path('exam_res/<int:id>/',exam_res,name='exam_res'),
]