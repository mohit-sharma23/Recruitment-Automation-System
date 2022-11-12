from django.shortcuts import render,redirect
from resume.models import resumedata,Candidate,Work_Experience,Course,Skill,Projects
from django.contrib.auth.models import User
from django.contrib import messages 

# Create your views here.

def candi_regis(request):
    if request.method =="POST":
        print(request.POST)
        candidate_name=request.POST['name']
        candidate_email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        username=request.POST['username']
        phno=request.POST['phone']
        address=request.POST['address']
        college=request.POST['college']
        cgpa=request.POST['cgpa']


        if Candidate.objects.filter(username=username):
            messages.error(request,"Company already exit please try diffrent id")
            print("1")
            return redirect('company_registration')
        if Candidate.objects.filter(candidate_email=candidate_email):
            messages.error(request,"Company email id is already exit!")
            print("2")
            return redirect('company_registration')
        if pass1 != pass2:
            messages.error(request, "Passwords didnt match!")
            print("3")
            return redirect('company_registration')

        candidate=Candidate(candidate_name=candidate_name,candidate_email=candidate_email,pass1=pass1,pass2=pass2,username=username,phno=phno,address=address,college=college,cgpa=cgpa)
        candidate.save()
        u=User(username=username,email=candidate_email,password=pass1)
        u.set_password(pass1)
        u.save()
        return redirect('login/')

    return render(request,'resume/candiRegist.html')

def candihome(request):
    return render(request,'resume/candiHome.html')

def create_resume(request):
    if request.method == "POST":
        print(request.POST)
        keys=list((request.POST).keys())
        user=Candidate.objects.get(username=request.user.username)
        for key in keys:
            temp=str(key)
            companyName=''
            WorkDetails=''
            Internship=False
            comp='comp'
            course='course'
            prj='prj'
            skill='skill'
            if comp in temp:
                companyName=request.POST.getlist(temp)[0]
                WorkDetails=request.POST.getlist(temp)[1]
                print(companyName)
                print(WorkDetails)
                if request.POST.getlist(temp)[2]=='Yes':
                    Internship=True
                else:
                    Internship=False
                workExp=Work_Experience(candidateId=user,companyName=companyName,workDetails=WorkDetails,internship=Internship)
                workExp.save()
            if course in temp:
                course=request.POST.getlist(temp)[0]
                platform=request.POST.getlist(temp)[1]
                courses=Course(candidateId=user,course=course,platform=platform)
                courses.save()
            if prj in temp:
                print(request.POST.getlist(temp))
                prj_name=request.POST.getlist(temp)[0]
                prj_link=request.POST.getlist(temp)[1]
                prj_des=request.POST.getlist(temp)[2]
                project=Projects(candidateId=user,prj_name=prj_name,prj_link=prj_link,prj_des=prj_des)
                project.save()
            if skill in skill:
                skill=request.POST.getlist(temp)[0]
                skills=Skill(candidateId=user,skill=skill)
                skills.save()

    return render(request, 'resume/createresume.html')