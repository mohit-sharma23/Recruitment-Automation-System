from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.
def check(request):
    return render(request,'AdminPanel/Check.html')
