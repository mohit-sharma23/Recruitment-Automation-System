from django.db import models
from Company.models import Companies
# Create your models here.
class resumedata(models.Model):
    name = models.CharField(max_length=20000)
    phno = models.CharField(max_length=1000)
    address = models.CharField(max_length=7000)
    college = models.CharField(max_length=4000)
    cgpa = models.CharField(max_length=2000)
    comname = models.CharField(max_length=40000)
    brief = models.CharField(max_length=200000)
    start = models.CharField(max_length=4000)
    end = models.CharField(max_length=4000)

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=20000)
    candidate_email=models.CharField(max_length=100)
    pass1=models.CharField(max_length=10,default="")
    pass2=models.CharField(max_length=10,default="")
    username=models.CharField(max_length=100,unique=True)
    phno = models.CharField(max_length=1000)
    address = models.CharField(max_length=7000)
    college = models.CharField(max_length=4000)
    cgpa = models.CharField(max_length=2000)

class Course(models.Model):
    candidateId=models.ForeignKey(Candidate,related_name='course',on_delete=models.CASCADE)
    course=models.TextField(max_length=100)
    platform=models.TextField(max_length=100,default='Edx')

class Skill(models.Model):
    candidateId=models.ForeignKey(Candidate,related_name='skill',on_delete=models.CASCADE)
    skill=models.TextField(max_length=100)

class Work_Experience(models.Model):
    candidateId=models.ForeignKey(Candidate,related_name='work',on_delete=models.CASCADE)
    companyName=models.TextField(max_length=100)
    workDetails=models.TextField(max_length=5000)
    internship=models.BooleanField(default=False)

class Projects(models.Model):
    candidateId=models.ForeignKey(Candidate,related_name='project',on_delete=models.CASCADE)
    prj_name=models.TextField(max_length=100)
    prj_link=models.TextField(max_length=100)
    prj_des=models.TextField(max_length=5000)



    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk}) 

