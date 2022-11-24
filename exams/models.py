from tkinter import CASCADE
from django.db import models
from Company.models import *
from resume.models import Candidate
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
    companyId=models.ForeignKey(Companies,related_name='comp',on_delete=models.CASCADE)
    jobId=models.ForeignKey(Job_Profiles,related_name='jo',on_delete=models.CASCADE,default=13)
    time=models.TimeField()

class ExamResult(models.Model):
    companyId=models.ForeignKey(Companies,related_name='compR',on_delete=models.CASCADE)
    jobId=models.ForeignKey(Job_Profiles,related_name='joR',on_delete=models.CASCADE,default=13)
    candidateId=models.ForeignKey(Candidate,related_name='can',on_delete=models.CASCADE)
    totalScore=models.FloatField()
