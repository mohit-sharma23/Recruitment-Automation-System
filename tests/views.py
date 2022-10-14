# from urllib import response
# from django.shortcuts import redirect, render
# from tests import models as QMODEL
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

# @login_required()
# def test_page(request,pk):
#     course=QMODEL.Course.objects.get(id=pk)
#     questions=QMODEL.Question.objects.filter(course=course)
#     if request.method=='POST':
#         pass
#     response= render(request,'testpage.html',{'course':course,'questions':questions})
#     response.set_cookie('course_id',1)
#     return response


# def calculate_marks_view(request): 
#         if request.COOKIES.get('course_id') is not None:
#             course_id = request.COOKIES.get('course_id')
#             course=QMODEL.Course.objects.get(id=course_id)
#             total_marks=0
#             questions=QMODEL.Question.objects.filter(course=course)
#             for i in range(len(questions)):
#                 selected_ans = request.COOKIES.get(str(i+1))
#                 actual_answer = questions[i].answer
#                 if selected_ans == actual_answer:
#                     total_marks = total_marks + questions[i].marks
#             result = QMODEL.Result()
#             result.marks=total_marks
#             result.exam=course
#             # result.student=
#             result.save()

#             if(result.marks > 0):
#                 return redirect("interview_offer")
#             else:
#                 return HttpResponse("Apki Aukad nahi ki Ap hai Company Join kar sake !!!!!!!!!!!!!!!!!!!!!!!!")    

# def interview_letter_view(request):
#     return render(request,"interview_offer.html")
