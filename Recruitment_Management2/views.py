from django.shortcuts import render
from pathlib import Path
from Company.models import Job_Profiles,Companies
from resume.models import Candidate,Resume
from exams.models import ExamResult


def home(request):
    print(Path(__file__).resolve().parent.parent)

    job=Job_Profiles.objects.all()
    num_can=len(Candidate.objects.all())
    num_res=len(Resume.objects.all())
    num_placed=len(ExamResult.objects.filter(status=True))
    jobs={
        'job':job,
        'num_can':num_can,
        'num_res':num_res,
        'num_placed':num_placed
    }
    return render(request,'Recruitment_management2/templates/Recruitment_management2/mainhome.html',jobs)

