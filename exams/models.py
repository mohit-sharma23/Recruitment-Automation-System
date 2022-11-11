from tkinter import CASCADE
from django.db import models
from Company.models import *
# Create your models here.
class Questions(models.Model):
    companyId=models.ForeignKey(Companies,related_name='company',on_delete=models.CASCADE)
    jobId=models.ForeignKey(Job_Profiles,related_name='job',on_delete=models.CASCADE,default=13)
    question=models.TextField()
    score=models.IntegerField()

class Options(models.Model):
    questionId=models.ForeignKey(Questions,related_name='questions',on_delete=models.CASCADE)
    option=models.TextField()

class Answers(models.Model):
    questionId=models.ForeignKey(Questions,related_name='ansQn',on_delete=models.CASCADE)
    optionId=models.ForeignKey(Options,related_name='ansOp',on_delete=models.CASCADE)

class ExamDuration(models.Model):
    time=models.TimeField()