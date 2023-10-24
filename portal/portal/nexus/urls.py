# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import StudentLoginView,HomeView

urlpatterns = [
    # ... other URL patterns ...
    path('home/', HomeView.as_view(), name='home'),  
    path('create-coordinator/', views.create_coordinator_view, name='create_coordinator'),
    path('coordinator-list/', views.coordinator_list, name='listr'),
    path('student/register/', views.student_registration, name='student_registration'),
    path('student/login/', StudentLoginView.as_view(), name='student_login'),
    path('student-list/', views.student_list, name='studentlist'),
    
    
    

  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)