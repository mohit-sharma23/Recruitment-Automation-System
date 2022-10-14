# from django.urls import path
# from candidates import views
# from django.contrib.auth.views import LoginView

# urlpatterns = [
#     path('candidate_registration/', views.candidate_registration, name="candidate_registration"),
#     path('candidate_multipage_registration/', views.candidate_registration_view, name="candidate_multipage_registration"),
#     path('candidate_login/', views.candidate_login, name="candidate_login"),
#     path('signOut/',views.signOut,name="signOut"),
#     path('candidate_home/',views.can_home,name="can_home"),
#     path('candidate_profile/',views.can_profile,name="can_profile"),
#     path('job_dis/<int:pk>',views.job_dis,name="job_dis"),
#     path('student-exam', views.student_exam_view, name='student-exam'),
#     path('take-exam/<int:pk>', views.take_exam_view, name='take-exam'),
#     path('start-exam/<int:pk>', views.start_exam_view, name='start-exam'),
#     path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
#     path('view-result', views.view_result_view, name='view-result'),
#     # path('check-marks/<int:pk>', views.check_marks_view, name='check-marks'),
#     # path('student-marks', views.student_marks_view, name='student-marks'),
# ]