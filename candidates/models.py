# import email
# from enum import unique
# from django.db import models
# from django.db import models
# from django.contrib.auth.models import User

# class Candidates(models.Model):
#     username = models.CharField(max_length=40,unique=True)
#     f_name = models.CharField(max_length=100)
#     l_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     mobile = models.CharField(max_length=10)
#     address = models.CharField(max_length=200)
#     hsc_school_name = models.CharField(max_length=100)
#     hsc_marks = models.PositiveIntegerField()
#     current_college_name = models.CharField(default="0",max_length=100)
#     college_cgpa = models.PositiveIntegerField(default="0")
#     resumeFile = models.FileField(upload_to=" ")

#     @property
#     def get_name(self):
#         return self.user.first_name+" "+self.user.last_name

#     @property
#     def get_instance(self):
#         return self

#     def __str__(self):
#         return self.user.username
