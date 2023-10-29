# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CoordinatorLoginView,TNPAdminLoginView

urlpatterns = [
    # ... other URL patterns ...
    path('home/', views.home, name='home'),  
    path('create-coordinator/', views.create_coordinator_view, name='create_coordinator'),
    path('create-coordinator/coordinator-list/', views.coordinator_list, name='listr'),
    path('student/register/', views.student_registration, name='student_registration'),
    path('student/login/', views.student_login, name='student_login'),
    path('student-list/', views.student_list, name='studentlist'),
    path('create-notice/', views.create_notice, name='createnotice'),
    path('coordinator/login/', CoordinatorLoginView.as_view(), name='coordinator_login'),
    path('tnp-admin/login/', TNPAdminLoginView.as_view(), name='tnp_admin_login'),
    path('cnotice-list/', views.c_notice_list, name='cnotice_list'),
    path('snotice-list/', views.s_notice_list, name='snotice_list'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('coordinator/login/', CoordinatorLoginView.as_view(), name='coordinator_login'),
    path('cnotice-list/delete/<int:notice_id>/', views.notice_delete, name='notice_delete'),
    
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)