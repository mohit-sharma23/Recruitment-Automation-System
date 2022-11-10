from django.shortcuts import render
from resume.models import resumedata

# Create your views here.
def create_resume(request):
    if request.method == "POST":
        username = request.POST['username']
        phno = request.POST['phone']
        address = request.POST['address']
        college = request.POST['college']
        cgpa = request.POST['cgpa']
        company = request.POST['company']
        brief = request.POST['brief']
        start = request.POST['start']
        end = request.POST['end']
        resum = resumedata(name = username, phno = phno, address=address, college = college,cgpa = cgpa,comname = company,brief = brief,start = start,end = end)
        print(resum)
        resum.save()
    return render(request, 'resume/createresume.html')