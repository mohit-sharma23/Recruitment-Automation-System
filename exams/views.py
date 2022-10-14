import re
from django.shortcuts import render
from .models import Questions,Options,Answers
from .forms import *


# Create your views here.


def form(request):
    if request.method=='POST':
        print(request.POST)
        # print("l")
        # print(request.POST.getlist('1')[1])
        keys=list((request.POST).keys())
        values=list((request.POST).values())

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
                print(request.POST.get(temp))
                # opt_id=Options.objects.get(questionId=qn_id,option=request.POST.get(temp))
                if(len(request.POST.getlist(temp))>1):
                    answers=Answers(questionId=Questions.objects.get(id=qn_id),optionId=Options.objects.get(id=opt_id))
                    answers.save()
                # continue
            else:
                questions=Questions(question=request.POST.getlist(temp)[0],score=request.POST.getlist(temp)[1])
                questions.save()
                qn_id=questions.id
                print(questions.id)


        # for key in keys[1:]:
        #     temp=str(key)
        #     us="_"
        #     if us in temp:
        #         ind=temp.index('_')
        #         qn=(temp[slice(0,ind)])
        #         print(temp[slice(ind+1,len(temp))])
        #         opt=int()
                # print(qn)
                # print(values[keys.index(key)])
                # print(request.POST.get(qn))
                # print(request.POST[qn]['1'])
                # qn_id=Questions.objects.get(question=request.POST.getlist(qn)[0])
                # # print(qn_id.id)
                # options=Options(questionId=qn_id,option=request.POST.get(temp))
                # options.save()
                # print(request.POST.get(temp))
                # opt_id=Options.objects.get(questionId=qn_id,option=request.POST.get(temp))
                # if(len(request.POST.getlist(temp))>1):
                #     answers=Answers(questionId=qn_id,optionId=opt_id)
                #     answers.save()
                    # print(hey)
                # print(qn)
                # print(opt)
            # else:
                # questions=Questions(question=request.POST[key],score=10)
                # questions.save()

    e=ExamForm
    o=OptionForm
    param={
        'e':e,
        'o':o,
    }
    return render(request,'exams/test.html',param)
