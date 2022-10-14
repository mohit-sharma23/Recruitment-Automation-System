# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.conf import settings
# from datetime import date, timedelta
# from tests import models as QMODEL
# from django.contrib.auth import authenticate, login, logout
# from django import template
# from django.template.defaultfilters import stringfilter
# from .forms import CandidateDetailsForm


# register = template.Library()
# # registering filter
# @register.filter
# @stringfilter
# def split(string, sep):
#     return string.split(sep)

# #for showing signup/login button for student
# def studentclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request, 'student/studentclick.html')

# # candidate login 
# def candidate_login(request):
#     if request.method == "POST":
#         success = True
#         if request.POST['username'] == "":
#             messages.error(request, "please fill empty field.")
#             return render(request, "loginpage.html", {'error': True})

#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authenticate(username=username, password=pass1)

#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             return redirect('can_home')
#         else:
#             messages.error(request, "Bad Credentials")
#             return redirect('candidate_login')
#     return render(request, 'templates/loginpage.html')

# #candidate registration
# def candidate_registration(request):
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         if User.objects.filter(username=username):
#             # messages.warning(request, "Username already exist! Please try some other username.")
#             messages.error(
#                 request,
#                 "Username already exist! Please try some other username.")
#             return redirect('candidate_registration')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email Already Registered!!")
#             return redirect('candidate_registration')

#         if len(username) > 20:
#             messages.error(request, "Username must be under 20 charcters!!")
#             return redirect('candidate_registration')

#         if pass1 != pass2:
#             messages.error(request, "Passwords didn't matched!!")
#             return redirect('candidate_registration')

#         if not username.isalnum():
#             messages.error(request, "Username must be Alpha-Numeric!!")
#             return redirect('candidate_registration')

#         newUser = User.objects.create_user(username, email, pass1)
#         newUser.first_name = fname
#         newUser.last_name = lname
#         newUser.save()

#         # messages.success(request,"Your account has been successfully created")

#         return redirect('candidate_login')
#     return render(request, 'registrationPage.html')

# def candidate_registration_view(request):
#     return render(request,"multipage_registration.html")
# # SignOut 
# def signOut(request):
#     logout(request)
#     return redirect('landingpage')

# # Candidate_Home
# @login_required()
# def can_home(request):
#     context = {
#         "user": request.user
#     }
#     return render(request,'candi_home.html',context)

# # candidate_Profile
# @login_required()
# def can_profile(request):
#     context = {
#         "user": request.user,
#         "form": CandidateDetailsForm()
#     }
#     return render(request,'candi_profile.html',context)

# #Job_Discription

# def job_dis(request,pk):
#     job_details = QMODEL.JobDescription.objects.get(jobs_id = pk)
#     print(job_details.id)
#     return render(request,'job_dis.html',{'job_details':job_details,'pk':pk})

# def is_student(user):
#     return user.groups.filter(name='STUDENT').exists()


# @user_passes_test(is_student)
# def student_dashboard_view(request):
#     dict = {
#         'total_course': QMODEL.Course.objects.all().count(),
#         'total_question': QMODEL.Question.objects.all().count(),
#     }
#     return render(request, 'student/student_dashboard.html', context=dict)


# @user_passes_test(is_student)
# def student_exam_view(request):
#     courses = QMODEL.Course.objects.all()
#     return render(request, 'student/student_exam.html', {'courses': courses})


# @user_passes_test(is_student)
# def take_exam_view(request, pk):
#     course = QMODEL.Course.objects.get(id=pk)
#     total_questions = QMODEL.Question.objects.all().filter(
#         course=course).count()
#     questions = QMODEL.Question.objects.all().filter(course=course)
#     total_marks = 0
#     for q in questions:
#         total_marks = total_marks + q.marks

#     return render(
#         request, 'student/take_exam.html', {
#             'course': course,
#             'total_questions': total_questions,
#             'total_marks': total_marks
#         })


# @user_passes_test(is_student)
# def start_exam_view(request, pk):
#     course = QMODEL.Course.objects.get(id=pk)
#     questions = QMODEL.Question.objects.all().filter(course=course)
#     if request.method == 'POST':
#         pass
#     response = render(request, 'student/start_exam.html', {
#         'course': course,
#         'questions': questions
#     })
#     response.set_cookie('course_id', course.id)
#     return response


# @user_passes_test(is_student)
# def calculate_marks_view(request):
#     if request.COOKIES.get('course_id') is not None:
#         course_id = request.COOKIES.get('course_id')
#         course = QMODEL.Course.objects.get(id=course_id)

#         total_marks = 0
#         questions = QMODEL.Question.objects.all().filter(course=course)
#         for i in range(len(questions)):

#             selected_ans = request.COOKIES.get(str(i + 1))
#             actual_answer = questions[i].answer
#             if selected_ans == actual_answer:
#                 total_marks = total_marks + questions[i].marks
#         result = QMODEL.Result()
#         result.marks = total_marks
#         result.exam = course
#         result.save()

#         return HttpResponseRedirect('view-result')


# @user_passes_test(is_student)
# def view_result_view(request):
#     courses = QMODEL.Course.objects.all()
#     return render(request, 'student/view_result.html', {'courses': courses})


# # @user_passes_test(is_student)
# # def check_marks_view(request,pk):
# #     course=QMODEL.Course.objects.get(id=pk)
# #     # results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
# #     return render(request,'student/check_marks.html',{'results':results})

# # @user_passes_test(is_student)
# # def student_marks_view(request):
# #     courses=QMODEL.Course.objects.all()
# #     return render(request,'student/student_marks.html',{'courses':courses})
