
from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from Recruitment_Management2 import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('exams.urls')),
    path('',include('resume.urls')),
    
    # path('',include('candidates.urls')),
    # path('',views.landingPage,name="landingpage"),
]

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)