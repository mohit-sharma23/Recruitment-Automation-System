<<<<<<< HEAD
from django.urls import path , include
from AdminPanel import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
   path('adminhome/',views.AdminHome,name='adminhome'),
   path('delcompany/<slug:pk>/',views.delcompany,name='delcompany'),
   path('candihomepage/',views.candihomepage,name='candihomepage'),
   path('delcandidate/<int:id>',views.delcandidate,name='delcandidate'),

   



=======
from AdminPanel import views
from django.urls import path , include
from django.conf import settings
from django.contrib import admin
urlpatterns=[
    path('',views.check,name='check'),
>>>>>>> b5d40e780e340922b1b12a474200ae8fc6ceef48
]