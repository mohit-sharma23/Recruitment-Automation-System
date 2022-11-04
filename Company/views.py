from email import message
from Company.models import Job_Profiles, Companies
from django.contrib import messages 

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from Company.models import Companies,Job_Profiles

# Create your views here.

def company_home(request):
    return render(request,'company.html')

#company registration
def company_registration(request):
    if request.method== 'POST':
        print(request)
        company_name=request.POST.get('cname')
        company_mobile_no=request.POST.get('mobileno')
        company_email=request.POST.get('email')
        companyuserid=request.POST.get('userid')
        state=request.POST.get('state')
        city=request.POST.get('city')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass1')

        if Companies.objects.filter(companyuserid=companyuserid):
            messages.error(request,"Company already exit please try diffrent id")
            print("1")
            return redirect('company_registration')
        if Companies.objects.filter(company_email=company_email):
            messages.error(request,"Company email id is already exit!")
            print("2")
            return redirect('company_registration')
        if password1 != password2:
            messages.error(request, "Passwords didnt match!")
            print("3")
            return redirect('company_registration')
            
        mycompany=Companies(company_name=company_name, company_contact_no=company_mobile_no,company_email=company_email,companyuserid=companyuserid,state=state,city=city,pass1=password1,pass2=password2)
        mycompany.save()
        u=User(username=companyuserid,email=company_email,password=password1)
        u.set_password(password1)
        u.save()

        return redirect('company')
        

    return render(request,'companyregistrationPage.html')

# def company_login(request):
#     if request.method=='POST':
#         print(request)
#         username=request.get('username')
#         password=request.get('pass1')
#         if(Companies.objects.filter(username=username)):
#             comp=Companies.objects.get(username=username)
#             pas=comp.pass1
#             if(password==pas):
#                 return render(request,'add.html')

def companyhome(request):
    return render(request,'company_dashboard.html')


def ADD(request):

    if request.method=='POST':
        job_role=request.POST.get('jobrole')
        job_des=request.POST.get('jobdes')
        vacancies=request.POST.get('vacancies')
        company_id=Companies.objects.get(companyuserid=request.user.username)
        data=Job_Profiles(profile_name=job_role,company_id=company_id,job_info=job_des,no_of_vacancies=vacancies)
        data.save()
        return redirect('add')
    info=Job_Profiles.objects.values('profile_name','job_info','no_of_vacancies')
    print(info)
    return render(request,'company_dashboard.html',{'company_info':info})

def delete(request,id):
    if request.method=='POST':
        role=Job_Profiles.objects.get(pk=id)
        role.delete()
        return redirect('add')
    return render(request,'company_dashboard.html')
