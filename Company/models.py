
from email.policy import default
from re import T
from django.db import models
from django.contrib.auth.models import User


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
    
        




    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.companyuserid
class Job_Profiles(models.Model):

    profile_name=models.CharField(max_length=100)
    company_id=models.ForeignKey("Companies",on_delete=models.CASCADE,default="0")
    job_info=models.TextField()
    salary=models.IntegerField(default="0")

    
    
    condi_tion=models.CharField(max_length=100)
    no_of_vacancies=models.CharField(max_length=100)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.profile_name
   



