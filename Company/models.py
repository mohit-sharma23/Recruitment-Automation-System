
from django.db import models
from django.contrib.auth.models import User
from resume.models import Candidate
from datetime import datetime

# Create your models here.

class Companies(models.Model):

    company_name=models.CharField(max_length=100)
    company_contact_no=models.CharField(max_length=100)
    company_email=models.CharField(max_length=100)
    companyuserid=models.CharField(max_length=100,unique=True,primary_key=True)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pass1=models.CharField(max_length=10,default="")
    pass2=models.CharField(max_length=10,default="")
    
class Job_Profiles(models.Model):
    profile_name=models.CharField(max_length=100)
    company_id=models.ForeignKey("Companies",on_delete=models.CASCADE)
    job_info=models.TextField()
    salary=models.CharField(max_length=100)
    no_of_vacancies=models.CharField(max_length=100)
    education=models.CharField(max_length=100)
    industry=models.CharField(max_length=100)
    joblocation_address=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    postdate=models.DateTimeField(default=datetime.now)
    site_name=models.CharField(max_length=100,default='NaN')

class industry(models.Model):
    industry=models.CharField(max_length=100)


class skills(models.Model):
    company_id=models.ForeignKey("Companies",on_delete=models.CASCADE)
    job_profile_id=models.ForeignKey("Job_Profiles",on_delete=models.CASCADE)
    skills=models.CharField(max_length=100)

    
    @property
    def get_instance(self):
        return self

class shortList(models.Model):
    job_id=models.ForeignKey(Job_Profiles,related_name='job_profile_id',on_delete=models.CASCADE)
    candidate_id=models.ForeignKey(Candidate,related_name='candi_id',on_delete=models.CASCADE)





