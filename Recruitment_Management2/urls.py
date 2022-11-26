
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from Recruitment_Management2 import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import home
urlpatterns = [
    path('admin', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='Recruitment_management2/templates/Recruitment_management2/company.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Recruitment_management2/templates/Recruitment_management2/mainhome.html'), name='logout-redirect'),
    path('',home,name='home'),
    path('candidate/',include('resume.urls')),
    path('exam/',include('exams.urls')),
    path('company/',include('Company.urls')),

    
    # path('',include('candidates.urls')),
    # path('',views.landingPage,name="landingpage"),
]

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)