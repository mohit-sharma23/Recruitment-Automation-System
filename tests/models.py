from django.db import models

# class Course(models.Model):
#    course_name = models.CharField(max_length=50)
#    question_number = models.PositiveIntegerField()
#    total_marks = models.PositiveIntegerField()
#    def __str__(self):
#         return self.course_name

# # class Question(models.Model):
# #     course=models.ForeignKey(Course,on_delete=models.CASCADE)
# #     marks=models.PositiveIntegerField()
# #     question=models.CharField(max_length=600)
# #     option1=models.CharField(max_length=200)
# #     option2=models.CharField(max_length=200)
# #     option3=models.CharField(max_length=200)
# #     option4=models.CharField(max_length=200)
# #     cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
# #     answer=models.CharField(max_length=200,choices=cat)

# # class Result(models.Model):
# #     # candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
# #     exam = models.ForeignKey(Course,on_delete=models.CASCADE)
# #     marks = models.PositiveIntegerField()
# #     date = models.DateTimeField(auto_now=True)

# class JobDescription(models.Model):
#     jobs = models.ForeignKey(Course,on_delete=models.CASCADE)
#     job_title = models.CharField(max_length=200)
#     job_discription = models.TextField(max_length=600)
#     applicable = models.TextField(max_length=600)
#     skills = models.CharField(max_length=200)
#     no_of_openings = models.CharField(max_length=200)
