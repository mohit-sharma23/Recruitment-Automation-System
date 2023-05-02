from django.db import models

from django.contrib.auth.models import User
from resume.models import Candidate
from Company.models import Companies
# Create your models here.
class Reports(models.Model):
    Candidate_name=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    Company_name=models.ForeignKey(Companies,on_delete=models.CASCADE)
    reason=models.CharField(max_length=1000)
    