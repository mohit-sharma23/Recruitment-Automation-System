from django.contrib import admin
from resume.models import resumedata,Candidate,Skill,Work_Experience,Course,Projects
# Register your models here.
admin.site.register(resumedata)
admin.site.register(Candidate)
admin.site.register(Skill)
admin.site.register(Work_Experience)
admin.site.register(Course)
admin.site.register(Projects)

