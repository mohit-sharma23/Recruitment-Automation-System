from email import message
from django.contrib import messages 

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from Company.models import Companies

# Create your views here.

def company_home(request):
    return render(request,'company.html')

#company registration
def company_registration(request):
    if request.method== 'POST':
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
            return redirect('company_registration')
        if Companies.objects.filter(company_email=company_email):
            messages.error(request,"Company email id is already exit!")
            return redirect('company_registration')
        if password1 != password2:
            messages.error(request, "Passwords didnt match!")
            return redirect('company_registration')
            
        mycomany=Companies(company_name=company_name, company_contact_no=company_mobile_no,company_email=company_email,companyuserid=companyuserid,state=state,city=city,pass1=password1,pass2=password2
        )
        
        mycomany.save()


        return redirect('company_registration')

    return render(request,'companyregistrationPage.html')