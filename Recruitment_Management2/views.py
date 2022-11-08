from django.shortcuts import render
from pathlib import Path



def home(request):
    print(Path(__file__).resolve().parent.parent)
    return render(request,'Recruitment_management2/templates/Recruitment_management2/mainhome.html')

