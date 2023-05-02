from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Company.models import Companies,Job_Profiles,shortList
from resume.models import Candidate,Course,Skill,Work_Experience,Projects
from exams.models import ExamResult,Questions,Options,Answers,ExamDuration
from .email import send_companyremoved_mail,send_candidate_removed_mail

# Create your views here.


def AdminHome(request):
   
   comlist= Companies.objects.all()
   totalcompanies=Companies.objects.all().count()
   totalcandidate=Candidate.objects.all().count()

   context={
       'comlist':comlist,
       'totalcompanies':totalcompanies,
       'totalcandidates':totalcandidate,
   }

   return render(request,'AdminPanel/admin.html',context)

def delcompany(request,pk):
    company=Companies.objects.get(companyuserid=pk)
    
    if company.delete():
        reciptent_list=company.company_email
        send_companyremoved_mail(reciptent_list)
        
    

    return redirect('adminhome') 

def candihomepage(request):
    candilist=Candidate.objects.all()
    context={
        'candilist':candilist

    }
    return render(request,'AdminPanel/candidate.html',context)
def delcandidate(request,id):
    candidate=Candidate.objects.get(id=id)
    if candidate.delete():
        reciptent_list_candi=candidate.candidate_email
        print(reciptent_list_candi)
        send_candidate_removed_mail(reciptent_list_candi)
        
    return redirect('candihomepage')
