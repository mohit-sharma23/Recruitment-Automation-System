from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from resume import views

urlpatterns = [
    path('',views.candi_regis,name='candi_regis'),
    path('candihome',views.candihome,name='candihome'),
    path('resume/',views.create_resume,name='create_resume'),
    path('apply_job/',views.apply_job,name='apply_job'),
    path('candi-profile/',views.candi_profile,name='candi_profile'),
    path('job-info/<int:id>',views.job_info,name='job_info'),
    path('update-resume',views.update_resume,name='update_resume'),
    path('del-exp',views.del_exp,name='del_exp'),
    path('del-course',views.del_course,name='del_course'),
    path('del-prj',views.del_prj,name='del_prj'),
    path('del-skill',views.del_skill,name='del_skill')

]