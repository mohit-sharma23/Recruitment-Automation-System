from django.shortcuts import render,redirect
from resume.models import resumedata,Candidate,Work_Experience,Course,Skill,Projects,Resume
from Company.models import Job_Profiles,skills,shortList
from exams.models import ExamResult
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    user=request.user.username
    candidate=Candidate.objects.get(username=user)
    CandiSkills=Skill.objects.filter(candidateId=candidate)
    FiltSkills=[]
    for s in CandiSkills:
        JobSkills=skills.objects.filter(skills=s.skill)
        for i in JobSkills:
            FiltSkills.append(i.job_profile_id)
    # print(FiltSkills)
    FSkills=set(FiltSkills)
    print(FSkills)
    job=Job_Profiles.objects.all()
    resume=Resume.objects.filter(candidateId=candidate)
    # print(resume)
    num_can=len(Candidate.objects.all())
    num_res=len(Resume.objects.all())
    num_placed=len(ExamResult.objects.filter(status=True))
    jobs={
        'job':job,
        'resume':resume,
        'num_can':num_can,
        'num_res':num_res,
        'FSkills':FSkills,
        'num_placed':num_placed
    }
    # if(skills):
        # print(skills)
    return render(request,'resume/candiHome.html',jobs)

def create_resume(request):
    
    if request.method == "POST":
        print(request.POST)
        keys=list((request.POST).keys())
        print(keys)
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
            if skill in temp:
                skill=request.POST.getlist(temp)[0]
                s=Skill(candidateId=user,skill=skill)
                s.save()
        CanRes=Resume.objects.filter(candidateId=user)
        print(CanRes)
        if CanRes.count() == 0:
            resume=Resume(candidateId=user)
            resume.save()
        return redirect('candihome')

    else:
        allSkills=skills.objects.values('skills').distinct()
        # print(allSkills)
        context={
            'skills':allSkills,
        }
        return render(request, 'resume/candiHome.html',context)

def apply_job(request):
    user=request.user.username
    candidate=Candidate.objects.get(username=user)
    jobs=ExamResult.objects.filter(candidateId=candidate)
    context={
        'jobs':jobs,
        'candidate':candidate
    }
    return render(request,'resume/jobs.html',context)

def candi_profile(request):
    candi=Candidate.objects.get(username=request.user.username)
    return render(request,'resume/candi_profile.html',{'candi':candi})

@login_required(login_url='login')
def job_info(request,id):
    job=Job_Profiles.objects.get(id=id)
    comp=job.company_id.company_name
    user=request.user.username
    candidate=Candidate.objects.get(username=user)
    resume=Resume.objects.filter(candidateId=candidate)
    s=skills.objects.filter(job_profile_id=job)
    print(resume)
    context={
        'job':job,
        'comp':comp,
        'resume':resume,
        's':s,
    }
    return render(request,'resume/jobdetail.html',context)

def update_resume(request):
    user=Candidate.objects.get(username=request.user.username)
    wrkExp=Work_Experience.objects.filter(candidateId=user)
    courses=Course.objects.filter(candidateId=user)
    prjs=Projects.objects.filter(candidateId=user)
    s=Skill.objects.filter(candidateId=user)
    allSkills=skills.objects.values('skills').distinct()

    context={
        'wrkExp':wrkExp,
        'courses':courses,
        'prjs':prjs,
        'skills':s,
        'allskills':allSkills,

    }
    return render(request,'resume/updateresume.html',context)

def del_exp(request):
    user=Candidate.objects.get(username=request.user.username)
    print('hello')
    Work_Experience.objects.filter(candidateId=user).delete()
    return redirect('update_resume')

def del_course(request):
    user=Candidate.objects.get(username=request.user.username)
    print('hello')
    Course.objects.filter(candidateId=user).delete()
    return redirect('update_resume')

def del_prj(request):
    user=Candidate.objects.get(username=request.user.username)
    print('hello')
    Projects.objects.filter(candidateId=user).delete()
    return redirect('update_resume')

def del_skill(request):
    user=Candidate.objects.get(username=request.user.username)
    print('hello')
    Skill.objects.filter(candidateId=user).delete()
    return redirect('update_resume')


def inter_offer(request,id):
    job=Job_Profiles.objects.get(id=id)
    context={
        'job':job,
    }
    return render(request,'resume/interview_offer.html',context)