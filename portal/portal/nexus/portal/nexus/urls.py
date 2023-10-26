# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,CoordinatorLoginView,TNPAdminLoginView,CombinedLoginView

urlpatterns = [
    # ... other URL patterns ...
    path('student/login/home/', HomeView.as_view(), name='home'),  
    path('create-coordinator/', views.create_coordinator_view, name='create_coordinator'),
    path('create-coordinator/coordinator-list/', views.coordinator_list, name='listr'),
    path('student/register/', views.student_registration, name='student_registration'),
    path('student/login/', CombinedLoginView, name='student_login'),
    path('student-list/', views.student_list, name='studentlist'),
    path('create-notice/', views.create_notice, name='createnotice'),
    path('coordinator/login/', CoordinatorLoginView.as_view(), name='coordinator_login'),
    path('tnp-admin/login/', TNPAdminLoginView.as_view(), name='tnp_admin_login'),
    path('notice-list/', views.notice_list, name='notice_list'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('apply_to_notice/<int:notice_id>/', views.apply_to_notice, name='apply_to_notice'),
    path('export-students-to-excel/', views.export_students_to_excel, name='export_students_to_excel')

    
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)