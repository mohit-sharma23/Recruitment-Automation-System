import re
from django.shortcuts import render,redirect
from .models import Questions,Options,Answers,ExamDuration
from Company.models import Companies,Job_Profiles
from .forms import *


# Create your views here.


def form(request,id):
    if request.method=='POST':
        # print(request.POST)
        # print("l")
        # print(request.POST.getlist('1')[1])
        keys=list((request.POST).keys())
        values=list((request.POST).values())
        username=request.user.username
        compId=Companies.objects.get(companyuserid=username)
        jobId=Job_Profiles.objects.get(id=id)
        # print(keys)
        # print(values)
        qn_id=0
        opt_id=0
        for key in keys[1:]:
            temp=str(key)
            us="_"
            if us in temp:
                ind=temp.index('_')
                qn=(temp[slice(0,ind)])
                print(temp[slice(ind+1,len(temp))])
                opt=int()
                # print(qn)
                # print(values[keys.index(key)])
                # print(request.POST.get(qn))
                # print(request.POST[qn]['1'])
                # qn_id=Questions.objects.get(question=request.POST.getlist(qn)[0])
                # print(qn_id.id)
                options=Options(questionId=Questions.objects.get(id=qn_id),option=request.POST.get(temp))
                options.save()
                opt_id=options.id
                # print(request.POST.get(temp))
                # opt_id=Options.objects.get(questionId=qn_id,option=request.POST.get(temp))
                if(len(request.POST.getlist(temp))>1):
                    answers=Answers(questionId=Questions.objects.get(id=qn_id),optionId=Options.objects.get(id=opt_id))
                    answers.save()
                # continue
            else:
                if(temp=='time'):
                    # print(request.get(temp))
                    examduration=ExamDuration(time=request.POST.get(temp))
                    examduration.save()
                else:
                    questions=Questions(companyId=compId,jobId=jobId,question=request.POST.getlist(temp)[0],score=request.POST.getlist(temp)[1])
                    questions.save()
                    qn_id=questions.id
                    print(questions.id)

    e=ExamForm
    o=OptionForm
    param={
        'e':e,
        'o':o,
    }
    return render(request,'exams/test.html',param)


def can_exam(request):
    question=Questions.objects.all()
    dur=str(ExamDuration.objects.get(id=2).time)
    # dur=dur[0:-3]
    qn_opts=[]
    for i in question:
        # print(question)
        opts=i.questions.all()
        qn_opts.append(opts)
    # context = {
    #     'questions':question,
    #     'qn_opts':qn_opts
    # }
    f=zip(question,qn_opts)
    # print(qn_opts)
    
    return render(request,'exams/canditest.html',{'f':f,'dur':dur})

def exam_res(request):
    if (request.method=="POST"):
        print("LLLLL")
        # print(request.POST)
        keys=request.POST.keys()
        totsc=0
        for key in keys:
            print('hello')
            ans=[]
            question=Questions.objects.get(id=key)
            score=question.score
            answers=question.ansQn.all()
            for a in answers:
                ans.append(a.optionId)
                # print(a.optionId)
            values=request.POST.getlist(key)
            options=Options.objects.filter(questionId=question)
            numopts=len(options)
            coropts=Answers.objects.filter(questionId=question)
            numans=len(coropts)
            percorans=score/numans
            sc=0
            # print(answers)
            for v in values:
                opt=Options.objects.get(id=v)
                # print(opt)
                if opt in ans:
                    print(opt)
                    sc+=percorans
                else:
                    sc=0
                    break
            totsc+=sc
            print(totsc)
        return redirect('home')