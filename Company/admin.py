from django.contrib import admin
from .models import Companies,Job_Profiles,skills
# Register your models here.
admin.site.register(Companies)
admin.site.register(Job_Profiles)
admin.site.register(skills)